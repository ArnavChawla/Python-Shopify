# Welcome to Shopi(Py)

Shopi(Py) was created to make it easy for people to interact with the frontend of Shopify Stores in Python. Whereas the current Shopify API allows store owners to interact with their stores backend, Shopi(Py) allows anybody to easily get information about stores and they're products

# Installation
The installation process for Shopi(Py) easy! Just enter the following command in your terminal:

`pip install shopi-py`

# Usage
Currently, the package is in early development and contains a few main methods. An example of usage is shown here:
	
	>>>import ShopiPy as shopify

	>>>url = "https://kith.com"

	>>>print(shopify.isShopify(url))
	True

	>>>print(shopify.findProductUrl(["Howie", "Short", "Blue"]))
	https://kith.com/products/khk6041-109

	>>>print(shopify.getSizeVariant("random"))
	19437737050240

	>>>print(shopify.getSizeVariant("6"))
	19437737148544
	
	>>>print(shopify.getCheckoutUrl())
	https://kith.com/checkout/19437737148544:1

# Feedback
This is my second public python package and I would appreciate any user feedback. For feature requests or changes, feel free to create an issue or pull request on the GitHub repo. 