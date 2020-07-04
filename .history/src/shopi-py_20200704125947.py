import RequestSoup as scraper

def isShopify(url):
    if url[-1] == "/":
        url = url + "admin"
    else:
        url = url + "/admin"
    r = scraper.get(url, allow_redirects=True)
    if "shopify" in r.url:
        return True
    return False

def findProduct(url, keywords):
    r = None
    if isShopify(url):
        if url[-1] == "/":
            r = scraper.get((url+"products.json")
