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

print(isShopify("https://google.com"))