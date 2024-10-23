from itertools import product

import requests
from dataclass_wizard import fromdict
from models.APIResponse import APIResponse
from models.product import Product
from vistas import ProductViewer


def main():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)

    viewer = ProductViewer(product_list.products)


main()
