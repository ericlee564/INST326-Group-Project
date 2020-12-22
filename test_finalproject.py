from finalproject import StoreInventory 
import pandas as pd

def test_update_stock():
    x = StoreInventory("inventory.csv", "Item_sold.csv")
    i = x.update_stocked()
    assert i.iloc[0]["Units Sold"] == 10
    assert i.loc[1]["Units Sold"] == 7
    assert i.loc[2]["Units Sold"] == 9
    assert i.loc[3]["Units Sold"] == 20
    assert i.loc[4]["Units Sold"] == 7
    
