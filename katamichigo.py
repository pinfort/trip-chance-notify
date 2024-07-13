import dataclasses

from libs.requests import getHtml
from libs.beautifulSoup import getBeautifulSoup, getTextFromClassName

TARGET_URL = "https://cp.toyota.jp/rentacar/"

@dataclasses.dataclass
class Car:
    shop_start: str
    shop_return: str
    date: str
    car_type: str
    condition: str
    info_date: str
    reserve: str
    expired: bool

def getCar(car) -> Car:
    shop_start = getTextFromClassName(car, "service-item__shop-start")
    shop_return = getTextFromClassName(car, "service-item__shop-return")
    date = getTextFromClassName(car, "service-item__date")
    car_type = getTextFromClassName(car, "service-item__info__car-type")
    condition = getTextFromClassName(car, "service-item__info__condition")
    info_date = getTextFromClassName(car, "service-item__info__date")
    reserve = getTextFromClassName(car, "service-item__reserve")
    expired = 'show-entry-end' in car.find(class_="service-item__body")['class']
    
    return Car(shop_start, shop_return, date, car_type, condition, info_date, reserve, expired)

cars: list[Car] = []

for car in getBeautifulSoup(getHtml(TARGET_URL)).find_all(class_="service-item"):
    cars.append(getCar(car)) #全車両取得

# 終了していない奴だけ表示
for valid_cars in filter(lambda x: not x.expired, cars):
    print(valid_cars)
