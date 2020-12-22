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
    
def test_low_inventory():
    x = StoreInventory('inventory.csv', 'item_sold.csv')
    lowest_number = x.low_inventory(10)
    assert lowest_number.iloc[0]['Item Name'] == 'Watermelon'
    middle_number = x.low_inventory(50)
    assert middle_number.iloc[0]['Item Name'] == 'Strawberry'
    assert middle_number.iloc[1]['Item Name'] == 'Blueberry'
    assert middle_number.iloc[3]['Item Name'] == 'Tomatoes'
    high_number = x.low_inventory(100)
    assert high_number.iloc[0]['Item Name'] == 'Strawberry'
    assert high_number.iloc[4]['Item Name'] == 'Lettuce'
    assert high_number.iloc[8]['Item Name'] == 'Chips'
    assert high_number.iloc[10]['Item Name'] == 'Gummy Worms'
    highest_number = x.low_inventory(300)
    assert highest_number.iloc[0]['Item Name'] == 'Strawberry'
    assert highest_number.iloc[4]['Item Name'] == 'Lettuce'
    assert highest_number.iloc[8]['Item Name'] == 'Chips'
    assert highest_number.iloc[10]['Item Name'] == 'Gum'
    assert highest_number.iloc[11]['Item Name'] == 'Water'
    assert highest_number.iloc[12]['Item Name'] == 'Cola'
    assert highest_number.iloc[13]['Item Name'] == 'Gummy Worms'
    
def test_stocked():
    x = StoreInventory("inventory.csv", "item_sold.csv")
    i = x.stocked()
    assert i.iloc[0]["Item Name"] == "Strawberry"
    assert i.iloc[1]["Item Name"] == "Blueberry"
    assert i.iloc[1]["Price ($)"] == 2.5 
    assert i.iloc[2]["Price ($)"] == 1.25
    assert i.iloc[2]["Amount"] == 75
    assert i.iloc[7]["Amount"] == 50