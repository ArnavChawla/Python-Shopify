import RequestSoup as scraper

def isShopify(url):
    if url[-1] == "/":
        url = url + "admin"
    else:
        url = url + "/admin"
    