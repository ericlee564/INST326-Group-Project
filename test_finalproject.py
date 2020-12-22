from finalproject import StoreInventory 
import pandas as pd

def test_update_stock():
    x = StoreInventory("inventory.csv", "Item_sold.csv")
    i = x.update_stocked()
    assert i.iloc[0]["Units Sold"] == 10
