from itertools import product
import requests
from dataclass_wizard import fromdict
from models.APIResponse import APIResponse
from models.empresa import Empresa
from models.product import Product
from vistas import ProductViewer


def generar_pdf(productos: list[Product]):
    empresa: Empresa = Empresa(
        nombre = "Simon Sofr S.L",
        titular= "SimonTech Industries Lopez",
        cif = "A1234568F",
        direccion = "calle rodolfo 49",
        email = "simonSoft@gmail.com"
    )






def main():
    respuesta = requests.get("https://dummyjson.com/products")
    datos_dict = respuesta.json()
    lista_productos = fromdict(APIResponse, datos_dict)


    visor = ProductViewer(lista_productos.products)


main()
