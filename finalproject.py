#Hyungik Lee, David McCoy, Noah Berman, Kiranpreet Kaur

from argparse import ArgumentParser
import sys
import pandas as pd

class StoreInventory():
    """Creates a pandas dataframes from csv files and uses these dataframes to alert the user
    of low inventory, generate potential coupons, and update the inventory based on items
    sold.
    
    Attributes:
        inventory_file(str): path to an inventory csv file
        items_sold_file(str): path to a items sold csv file
    """
    def __init__(self, inventory_file, items_sold_file):
        self.inventory_file = inventory_file
        self.items_sold_file = items_sold_file 
        
    def stocked(self):
        """
        This function keeps tracks of how many item we have in our current stock 
        by different categories
        Return: 
            Pandas dataframe of the inventory  
        """
        data = pd.read_csv(self.inventory_file, sep=",")
        cols =["Item Name","Category", "Amount","Price ($)"]
        df2 = data[cols]
        return df2
    
    def low_inventory(self, limit):
        '''Print the name of item that is running low. The amount that is defined as running
        low is based on the limit.
        
        Arg:
            limit(int): integer number of when the user thinks an item amount is too low
        
        Return:
            Dataframe of items based less than or equal to the limit. 
        '''
        stocked = self.stocked()
        low_inventory = stocked[stocked["Amount"]<=int(limit)]
        return low_inventory
        
    def coupon_generator(self):
        """Creates coupon for specific category of food based off how much is left
        in the inventory
        
        Returns:
            Dataframe of information for the item(s) discounted and their discounted price.
        """
        stocked = self.stocked()
        limited = stocked[stocked['Amount'] < 30]

        limited['Price ($)'] *= 0.85
        return limited
        
    def item_display(self):
        """Displays categorized products, quantities, and prices based on user request.
            
        Returns: 
            List of products by category"""
        
        print("Enter category to view products (Fruits, Vegetable, Snacks, Drinks): ")
        cat = str(input())
        stocked = self.stocked()
        selected = stocked[stocked['Category'] == cat]
        return selected
    
    def num_item_sold(self):
        """This function keeps tracks of number of all items sold
        
        Return:
            Dataframe of the name of items sold and how many units of each was sold    
        """
        data1 = pd.read_csv(self.items_sold_file, sep=",")
        col =["Item Name","Units Sold"]
        df3 = data1[col]
        return df3
    
    def update_stocked(self):
        """Updates the dataframe returned from stocked method according to the dataframe 
        returned by the num_item_sold dataframe
            
        Return:
            Dataframe of updated stocked items      
        """        
        stocked = self.stocked()     
        units_sold = self.num_item_sold()       
        updated_df = stocked.merge(units_sold, on = "Item Name")  
        updated_df["Amount"] = updated_df["Amount"] - updated_df["Units Sold"]           
        return updated_df

def option():
    '''Instruction for the user to prompt them to next steps in checking inventory
    
    Return:
        Strings of instructions
    '''
    print("*************************************")
    print("\tStore's Inventory")
    print("*************************************")
    print("\t1.Show All Products")
    print("\t2.Low Stock")
    print("\t3.Number of item sold")
    print("\t4.Updated Stock")
    print("\t5.Generate Coupons")
    print("\t6.Item Discount")
    print("**************************************")    
    

def main(inventory_file, items_sold_file):
    """Builds a dataframe using two files and using different functions, provides information 
    about the inventory
    
    Args:
        inventory_file(str): path to a inventory file
        items_sold_file(str): path to a number of items sold file
    
    Return:
        A dataframe depending on what the user selects in the option() function
    """
    option()
    choice = int(input())
    x = StoreInventory(inventory_file, items_sold_file)
    if choice == 1:
        g = x.stocked()
        print("Number of items in the current stock\n")
        print (g)
    elif choice == 2:
        limit = input('Low Inventory Number: ')
        g = x.low_inventory(limit)  
        print(g)
    elif choice == 3:
        g = x.num_item_sold()
        print(g)
    elif choice == 4:
        g = x.update_stocked()
        print(g)
    elif choice == 5:
        g = x.coupon_generator()
        print(g)
    elif choice == 6:
        g = x.item_display()
        print(g)

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("inventory_filename", help="path to Inventory CSV file")
    parser.add_argument("items_sold_filename", help="path to Item Sold CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.inventory_filename, args.items_sold_filename)
        

    
    
    