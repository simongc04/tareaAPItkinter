from itertools import product

import requests
from dataclass_wizard import fromdict
from models import APIResponse

response = requests.get("https://dummyjson.com/products")
data_dict = response.json()
data_obj = fromdict(APIresponsave, data_dict)
print(data_obj.total)


