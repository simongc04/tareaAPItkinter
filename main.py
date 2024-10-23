from itertools import product

import requests
from dataclass_wizard import fromdict
from models.APIResponse import APIResponse
from models.product import Product
from vistas import mostrar_producto


def main():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)
    mostrar_producto(product_list.products[0])
    # for Product in product_list.products:
    #     print(Product.title)
    #     for review in Product.reviews:
    #         print(review.comment)
    #     print()

main()
