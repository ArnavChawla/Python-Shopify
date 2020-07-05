# -*- coding: utf-8 -*-
import RequestSoup as scraper
import json,random

fproduct = None
fvariant = None
furl = None

class size():
    def __init__(self, variant, sizen):
        self.variant = variant
        self.sizes = sizen

def isShopify(url):
    #Checks if a store is hosted on the shopify platforn 
    if url[-1] == '/':
        url = url + 'admin'
    else:
        url = url + '/admin'
    r = scraper.get(url, allow_redirects=True)
    if 'shopify' in r.url:
        global furl
        furl = url
        return True
    return False


def getProduct(keywords, url=None):
    if url == None:
        url = furl
    r = None
    if isShopify(url):
        if url[-1] == '/':
            r = scraper.get(url + 'products.json')
            
        else:
            r = scraper.get(url + '/products.json')

        if r.status_code != 200:
            raise Exception('Error retriving products: special site or password page present')

        else:
            products_json = json.loads(r.text)
            products = products_json['products']
            for product in products:
                keys = 0
                for keyword in keywords:
                    if keyword.upper() in product['title'].upper():
                        keys += 1
                    if keys == len(keywords):
                        global fproduct
                        fproduct = product
                        return product


def findProductUrl(keywords, url=None):
    #Returns the URL of a product given the site 
    if url == None:
        global furl
        url = furl
    product = getProduct(url, keywords)
    if product != None:
        if url[-1] == '/':
            return url + '{}'.format(product['handle'])
        return url + '/{}'.format(product['handle'])
    return 'Product Not Found'

def findVariant(product, size):
    if size.lower() != 'random':
        for variant in product['variants']:
            if size in variant['title']:
                variant = str(variant['id'])
                global fvariant
                fvariant = variant
                return variant
    else:
        variants = []
        for variant in product["variants"]:
            variants.append(size(variant["id"], variant["title"]))
        variant = random.choice(variants)
        strv = variant.variant
        return strv

def getSizeVariant(size, url=None, keywords=None):
    # Get the specific Variant for a product size. This can be used to generate Add to Cart Links
    if url == None or keywords == None:
        global fproduct
        product = fproduct
        return findVariant(product, size)
    else:
        product = getProduct(url,keywords)
        return findVariant(product, size)

def getCheckoutUrl(variant=None,url=None,keywords=None,size=None):
    # Generate a Checkout URL for a product
    if variant != None:
        if url == None:
            if url[-1] == "/":
                return scraper.get("{}cart{}:1".format(url,variant),allow_redirects=True).url
            else:
                return scraper.get("{}/cart{}:1".format(url, variant),allow_redirects=True).url
    elif variant == None and keywords != None:
        product = None
        if url == None:
            global furl
            url = furl
            product = getProduct(keywords,url)
        else:
            product = getProduct(keywords,url)
        if size == None:
            variant = getSizeVariant("random",url)
            if url[-1] == "/":
                return scraper.get("{}cart{}:1".format(url, variant), allow_redirects=True).url
            else:
                return scraper.get("{}/cart{}:1".format(url, variant), allow_redirects=True).url
    
