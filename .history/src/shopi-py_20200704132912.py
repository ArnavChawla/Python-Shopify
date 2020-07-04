import RequestSoup as scraper
import json
fproduct = None
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
        if r.status_code != 200:
            raise Exception("Error retriving products: special site or password page present")
        else:
            products_json = json.loads(r.text)
            products = products_json["products"]
            for product in products:
                keys = 0
            for keyword in keywords:
                if(keyword.upper() in product["title"].upper()):
                    keys += 1
                if(keys == len(keywords)):
                    global fproduct
                    fproduct = product
                    return url + "/{}".format(product["handle"])
print(findProduct("https://thistesting.myshopify.com/",["blue"]))
