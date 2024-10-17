from models import review
from models.dimensions import Dimensions
from models import meta
from dataclasses import dataclass


@dataclass

class Product:
        id: int
        title: str
        description :  str
        category : str
        price : int
        discountPercentage : int
        rating : int
        stock : int
        tags : str
        brand : str
        sku : str
        weight : int
        dimensions : Dimensions
        warrantyInformation : str
        shippingInformation : str
        availabilityStatus : str
        reviews : [review]
        returnPolicy : str
        minimumOrderQuantity : int
        meta : Meta
        images : str
        thumbnail : str
