from re import I
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# Istances of Vendor:
vendor = Vendor()
vendor_1 = Vendor(inventory=["item_1","item_2","item_3"])

# Instance of Item:
item_1 = Item(category='decor')
item_2 = Item(category='clothing', condition=3)


