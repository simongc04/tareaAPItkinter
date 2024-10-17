from typing import List

from models.review import Review
from models.dimensions import Dimensions
from models.meta import Meta
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
        reviews : List[Review]
        returnPolicy : str
        minimumOrderQuantity : int
        meta : Meta
        images : str
        thumbnail : str
