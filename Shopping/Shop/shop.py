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