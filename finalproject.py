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
    def __init__(self, filename):
        self.conn = sqlite3.connect(':memory:')
        self.addinventory(filename)
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass
    def addinventory(self, filename):
        """ Creates a database of an inventory using a csv file
        
        Args:
            filename (str): name of file
        Side Effects:
            Creation of database
        """
        cursor = self.conn.cursor()
        cq = '''CREATE TABLE inventory
                (item text, price real, amount integer, category text)'''
        cursor.execute(cq)
        with open(filename, 'r', encoding = 'utf-8') as f:
            headers = next(f)
            for row in f:
                values = row.strip().split(',')
                data = (values[0], float(values[1]), int(values[2]), values[3])
                item, price, amount, category = data
                iq = '''INSERT INTO inventory VALUES (?,?,?,?)'''
                cursor.execute(iq, data)
        self.conn.commit()
    def order_more(self, limit):
        '''Print the name of item that is running low. The amount that is defined as running
        low is based on the limit.
        
        Arg:
            limit(int): integer number of when the user thinks an item amount is too low
        
        Return:
            String of items that are equal to the limit. 
        '''
        cursor = self.conn.cursor()
        sq = f"SELECT item FROM inventory WHERE amount = {limit}"
        goods = cursor.execute(sq).fetchall()
        for good in goods:
            for item in good:
                print(f'Order more {item}')
        
    def stocked(self, filename):
        """
        This function keeps tracks of how many item we have in our current stock 
        by different categories
        Args:
            filename (str): name of the file     
        """
        data = pd.read_csv(filename, sep=",",index_col="Category")
        cols =["Item Name","Amount","Price ($)"]
        df2 = data[cols]
        return df2

    def coupon_generator(self):
        """Creates coupon for specific category of food based off how much is left
        in the inventory
        Args:
            item (str): name of item for coupon
            category (str): type of category of food within grocery store
        Returns:
            string of information for the item(s) discounted
        """
        cursor = self.conn.cursor()
        selected = f"SELECT item FROM inventory WHERE amount < {30}"
        limited = cursor.execute(selected).fetchall()
        
        for items in limited:
            for product in items:
                cursor.execute(f"UPDATE inventory SET price = price * {.85} WHERE amount < {30}")
                return f"15% off {product} while supplies last"

    def item_discount(self):
        """Generates discount for chosen item based on category and allows 
        customer to pay reduced price for product.
            
        Returns: 
            String with the discounted product"""
        
        print("Enter category for discount (Fruits, Vegetables, Snacks, Drinks): ")
        cat = str(input())
        
        cursor = self.conn.cursor()
        selected = f"SELECT item FROM inventory WHERE category = '{cat}'"
        catList = cursor.execute(selected).fetchall()
        
        # update the inventory with discounted item
        
        return catList
            
    def num_item_sold(self, filename):
        """This function keeps tracks of number of all items sold and updates the database 
            Args:
                item(int): different item types in the stock
                amountsold(int): number of items sold 
        """
        data1 = pd.read_csv("Item_sold.csv", sep=",")
        col =["Item Name","Units Sold"]
        df3 = data1[col]
        return df3
    
    def update_stocked(self, filename, item_sold_file):
        """      
        """        
        stocked = self.stocked(filename)        
        units_sold = self.num_item_sold(item_sold_file)       
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
    

def main(filename):
    """Build a database according to the file and take user input to decide the minimum of each 
    item before more needs to be ordered
    
    Args:
        filename(str): path to a file
    
    Return:
        A string of an item that needs to be ordered
    """
    e = StoreInventory(filename)
    limit = int(input('Limit: '))
    return e.order_more(limit)

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("inventory_filename", help="path to Inventory CSV file")
    parser.add_argument("items_sold_filename", help="path to Item Sold CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    option()
    choice = int(input())
    x = StoreInventory(args.inventory_filename)
    if choice == 1:
        g = x.stocked(args.inventory_filename)
        print("Number of items in the current stock\n")
        print (g)
    elif choice == 2:
        main(args.inventory_filename)  
    elif choice == 3:
        g = x.num_item_sold(args.items_sold_filename)
        print(g)
    elif choice == 4:
        g = x.update_stocked(args.inventory_filename, args.items_sold_filename)
        print(g)
    elif choice == 5:
        g = x.coupon_generator()
        print(g)
    elif choice == 6:
        g = x.item_discount()
        print(g)
        

    
    
    