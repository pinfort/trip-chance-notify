import requests

def getHtml(url: str) -> str:
    return requests.get(url).text
