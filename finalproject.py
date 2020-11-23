#Hyungik Lee, David McCoy, Noah Berman, Kiranpreet Kaur

from argparse import ArgumentParser
import sys

class store():
    """Creates a dictionary of inventory from given file
    Attributes:
        """
    def __init__(self):
        self.inventory = dict()
        
    def inventory(self, item, price, amount):
         """ Creates a dictionary of all products within the store and its prices
        
        Args:
            item(str): string of item name
            price(int): price of item
            amount(int): number of items in inventory
        Returns:
            final_inventory(dict) : dictionary of all items
        """
    
    def addinventory(self, filename):
        """ Allows employees to add products to current inventory list
        
        Args:
            filename (str): name of file
        Returns:
            final_updated_inventory(dict): returns updated inventory
        """
        with open(filename, 'r', encoding = 'utf-8') as f:
            headers = next(f)
            for line in f:
                strip = line.strip()
                split = strip.split(',')
                item = split[0]
                price = split[1]
                amount = split[2]
                category = split[3]
                self.inventory['Item'] = item
                self.inventory['Item'][item] = {'Price': price, 'Amount': amount, 'Category': category}
    def order(self, limit=10):
    """Creates an inventory of items that are running low
    
    Args:
        limit(int): amount of inventory that the user needs to order more at
    Returns:
        order_list(list): list of items that need to be ordered
    """

        if self.inventory['Amount'] =< limit:
            return f'Order more {self.inventory['Item']}'
        else:
            pass
        
def stocked(limit,categories):
    """
    This function keeps tracks of how many item we have in our current stock 
    by different categories
    Args:
        limit(int): Number of items store have in the stock
        categories(list): different categories in the stock
    
    """
    
def num_item_sold(item, amountsold):
    """This function keeps tracks of number of all items sold 
    Args:
        item(int): different item types in the stock
        amountsold(int): number of items sold 
    """    
        
def item_discount(total_cost):
    """Generates a discount on the items ordered
    Args:
        total_cost (float): total cost of all items ordered
    Returns: 
        String with the given discount for specific product"""
        
def coupon_generator(item, category):
    """Creates coupon for specific category of food
    Args:
        item (str): name of item for coupon
        category (str): type of category of food within grocery store
    Returns:
        String of the item discounted"""

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="path to Inventory CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

    
    
    