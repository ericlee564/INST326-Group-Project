#Hyungik Lee, David McCoy, Noah Berman, Kiranpreet Kaur

from argparse import ArgumentParser
import sys
import sqlite3
import pandas as pd

class StoreInventory():
    """Creates a database connection of an inventory from given file and uses different
    capabilities to let the user work with the inventory
    Attributes:
        self.conn: in memory database connection
        """
    def __init__(self, inventory_file, items_sold_file):
        self.inventory_file = inventory_file
        self.items_sold_file = items_sold_file 
        
    def stocked(self):
        """
        This function keeps tracks of how many item we have in our current stock 
        by different categories
        Args:
            filename (str): name of the file     
        """
        data = pd.read_csv(self.inventory_file, sep=",",index_col="Category")
        cols =["Item Name","Amount","Price ($)"]
        df2 = data[cols]
        return df2
    
    def low_inventory(self, limit):
        '''Print the name of item that is running low. The amount that is defined as running
        low is based on the limit.
        
        Arg:
            limit(int): integer number of when the user thinks an item amount is too low
        
        Return:
            String of items that are equal to the limit. 
        '''
        stocked = self.stocked()
        low_inventory = stocked[stocked["Amount"]<=int(limit)]
        return low_inventory
        
    def coupon_generator(self):
        """Creates coupon for specific category of food based off how much is left
        in the inventory
        Args:
            item (str): name of item for coupon
            category (str): type of category of food within grocery store
        Returns:
            string of information for the item(s) discounted
        """
        stocked = self.stocked()
        limited = stocked[stocked['Amount']<30]
        #Updates with 15% off product
        limited['Price ($)'] *= 0.85
        return limited
        

    def item_discount(self,total_cost):
        """Generates a discount on certain items ordered and allows 
        customer to pay reduced price for product. Updates total cost.
        Args:
            total_cost (float): total cost of all items ordered
        Returns: 
            String with the given discount for specific product"""
    
    def num_item_sold(self):
        """This function keeps tracks of number of all items sold and updates the database 
            Args:
                item(int): different item types in the stock
                amountsold(int): number of items sold 
        """
        data1 = pd.read_csv(self.items_sold_file, sep=",")
        col =["Item Name","Units Sold"]
        df3 = data1[col]
        return df3
    
    def update_stocked(self):
        """Updates the dataframe returned from stocked method according to the dataframe 
        returned by the num_item_sold dataframe
        
        Args 
            inventory_file(str): path to inventory csv
            item_sold_file(str): path to sold items csv
            
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
    print("**************************************")    
    

def main(inventory_file, items_sold_file):
    """Build a database according to the file and take user input to decide the minimum of each 
    item before more needs to be ordered
    
    Args:
        filename(str): path to a file
    
    Return:
        A string of an item that needs to be ordered
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

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("inventory_filename", help="path to Inventory CSV file")
    parser.add_argument("items_sold_filename", help="path to Item Sold CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.inventory_filename, args.items_sold_filename)
        

    
    
    