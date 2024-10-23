from itertools import product
import requests
from dataclass_wizard import fromdict
from models.APIResponse import APIResponse
from models.product import Product
from vistas import ProductViewer


def main():
    respuesta = requests.get("https://dummyjson.com/products")
    datos_dict = respuesta.json()
    lista_productos = fromdict(APIResponse, datos_dict)


    visor = ProductViewer(lista_productos.products)


main()
