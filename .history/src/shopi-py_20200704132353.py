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
            r = scraper.get((url+"products.json"))
        else:
            r = scraper.get((url+"/products.json"))
        if r.response_code != 200:
            raise Exception("Error retriving products: special site or password page present")
        else:
            for product in products:
                keys = 0
            for keyword in keywords:
                if(keyword.upper() in product["title"].upper()):
                    keys += 1
                    global p_name
                    p_name = product["title"]
                if(keys == len(keywords) and product["variants"][0]["available"] != False):
                    return product