#Hyungik Lee, David McCoy, Noah Berman, Kiranpreet Kaur

from argparse import ArgumentParser
import sys

class StoreInventory():
    """Creates a dictionary of inventory from given file
    Attributes:
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
        """ Allows employees to add products to current inventory list
        
        Args:
            filename (str): name of file
        Returns:
            final_updated_inventory(dict): returns updated inventory
        """
        cursor = self.conn.cursor()
        cq = '''CREATE TABLE inventory
                (item text, price real, amount integer, category text)'''
        cursor.execute(cq)
        with open(filename, 'r', encoding = 'utf-8') as f:
            headers = next(f)
            for row in f:
                values = row.split(',')
                data = (values[0], float(values[1]), int(values[2]), values[3])
                item, price, amount, category = data
                iq = '''INSERT INTO inventory VALUES (?,?,?,?)'''
                cursor.execute(iq, data)
        self.conn.commit()
    def order_more(self, limit):
        cursor = self.conn.cursor()
        sq = f"SELECT item FROM inventory WHERE amount = {limit}"
        goods = cursor.execute(sq).fetchall()
        print(goods)
        
    def stocked(limit,categories):
        """
        This function keeps tracks of how many item we have in our current stock 
        by different categories
        Args:
            limit(int): Number of items store have in the stock
            categories(list): different categories in the stock
    
        """

    def coupon_generator(item, category):
    """Creates coupon for specific category of food
    Args:
        item (str): name of item for coupon
        category (str): type of category of food within grocery store
    Returns:
        String of the item discounted"""

    def item_discount(total_cost):
    """Generates a discount on the items ordered
    Args:
        total_cost (float): total cost of all items ordered
    Returns: 
        String with the given discount for specific product"""
    
def num_item_sold(item, amountsold):
    """This function keeps tracks of number of all items sold and updates the database 
    Args:
        item(int): different item types in the stock
        amountsold(int): number of items sold 
    """    
       
def main(filename):
    e = StoreInventory(filename)
    limit = 10
    return e.order_more(limit)

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="path to Inventory CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)

    
    
    