"""Class Shop file."""
from customer import Customer
from product import Product



class Shop:
    """Class shop."""
    
    def __init__(self, name) -> None:
        """Constructor for class Shop.
        
        param: name
        output: None"""
        self.name = name
        self.storage = list[Product]
        self.sale = {}
        self.coupon = {}
        
        
    def can_add_storage(self, product: Product) -> bool:
        """Check if product can be added to storage.
        
        If item can not be added to storage then raise ValueError.
        
        param: prodcut
        output: bool"""
        if isinstance(product, Product):
            return True
        else:
            raise ValueError("Only Product objects can be added to storage.")
        
    def add_storage(self, product: Product) -> None:
        """Add item to storage if it can be added.
        
        If item was not added to the storage let user know.
        
        param: product
        output: None"""
        try:
            self.can_add_storage(product)
            self.storage.append(product)
        except ValueError as e:
            print(f"Operation unsuccessful: {e}")
            
    def storage_filter(self, name: str=None, weight: float=None,price_min: float=None, price_max: float=None, product_type: list=None, ascending: bool=True) -> list:
        """Filter storage based on parameters given
        
        one or many filters can be applied and used to filter the storage
        if price min and price max is given always have prices in ascending order if not said otherwise
        
        param: name
        param: weight
        param: price_min
        param: price_max
        param: product_type
        param: ascending
        output: list"""
        
        filtered_storage = []
        for product in self.shoppingcart:
            if name and product.name != name:
                continue
            if weight and product.weight != weight:
                continue
            if price_min and product.price < price_min:
                continue
            if price_max and product.price > price_max:
                continue
            if product_type and product.product_type not in product_type:
                continue
            filtered_storage.append(product)
        if ascending:
            filtered_storage.sort(key=lambda x: (x.price, x.name))
        else:
            filtered_storage.sort(key=lambda x: (x.price, x.name), reverse=True)
        return filtered_storage
    
    
    def add_sale(self, name: str, amount: int= 10) -> None:
        """Add item to sale.
        
        If item is already on sale then ask if person wants to overwrite the sale
        If item sale is 0 then remove from the sale dictionary
        Item sale amount is in % and can't be negative nor higher than 100
        if amount is higher than 100 ValueError is raised
        
        param: name
        param: amount
        output: None"""
        if -1 < amount < 101 and name in list(self.sale.keys()):
            while True:
                answer = input(f"You are about to overwrite {name} sale amount are you sure Y/N")
                if answer.upper() != "Y" or answer.upper() != "N":
                    print("Incorrect input!")
                if answer.upper() == "Y":
                    print("Change successful")
                    self.sale[name] = amount
                if answer.upper() == "N":
                    print("Operation aborted")
                    break
        if -1 < amount < 101 and name not in list(self.sale.keys()):
            print("Operation successful!")
            self.sale[name] = amount
        raise ValueError("Sale amount can only be between 0 and 100")
            
    def add_coupon(self, coupun, amount) -> None:
        """Add copun code to store.
        
        if coupun code is already there ask if user is sure he want's to overwrite the coupun
        copun gives discount in % so the amount can't be over 100 nor under 0
        
        param: coupun
        param: amount
        output: None"""
        
        if -1 < amount < 101 and coupun in list(self.coupon.keys()):
            while True:
                answer = input(f"You are about to overwrite {coupun} sale % are you sure Y/N")
                if answer.upper() != "N" or answer.upper() != "Y":
                    print("Incorrect input!")
                if answer.upper() == "Y":
                    print("Change successful")
                    self.coupon[coupun] = amount
                    break
                if answer.upper() == "N":
                    print("Operation aborted")
                    break
                
    def checkout(self):
        """"""
