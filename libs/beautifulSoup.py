from bs4 import BeautifulSoup

def getBeautifulSoup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')

def getTextFromClassName(soup, class_: str) -> str:
    return soup.find(class_=class_).get_text(strip=True)
