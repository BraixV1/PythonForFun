"""Class product file."""




class Product:
    
    def __init__(self, name: str, price: float, weight: float, amount: int, description: str=None, product_type: str=None) -> None:
        """Constructor of product class.
        
        param: name
        param: price
        param: weight
        param: descritpion
        param: type
        param: amount
        """
        
        self.name = name
        self.set_price(price)
        self.set_weight(weight)
        self.description = description
        self.type = product_type
        self.amount = amount
        
        
    def __repr__(self) -> str:
        """Reprsentor of product class."""
        
        return f"name: {self.name}, price: {self.price}, weight: {self.weight}, description: {self.description}"
    
    
    def add_description(self, description: str) -> None:
        """Overwrite the desceiprion of an item.
        
        Asks if user is sure he or she wants to ovwrwrite the item description:
        
        param: input:str
        output: None
        """
        if self.description is not None:
            answer = input(f"Are you sure you want to overwrite {self.name} description Y/N ")
            while True:
                if  answer.upper() is not "N" or answer.upper() is not "Y":
                    answer = input(f"Unknown input only possible inputs are Y/N")
                if answer.upper() is "Y":
                    self.description = description
                    break
                if answer.upper() is "N":
                    break
        else:
            self.description = description
            
                    
    def set_price(self, new_price: float) -> None:
        """Set price of a product:
        
        if new price set is negative raise ValueError
        
        param: new_price
        output: None"""
        if new_price < 0:
            raise ValueError("Price can't be negative")
        else:
            self.price = round(new_price, 2)
            
            
    def set_type(self, type:str) -> None:
        """Change product type
        
        if already has a type ask if user is sure that if he want's to change it.
        
        param: type
        output: None
        """
        if self.type is not None:
            answer = input(f"Are you sure you want to overwrite {self.name} type Y/N ")
            while True:
                if  answer.upper() is not "N" or answer.upper() is not "Y":
                    answer = input(f"Unknown input only possible inputs are Y/N")
                if answer.upper() is "Y":
                    self.description = type
                    break
                if answer.upper() is "N":
                    break
        else:
            self.type = type
            
            
    def set_weight(self, weight: float) -> None:
        """set new weight for product.
        
        if weight is smaller than 0 then raise ValueError.
        
        param: weight
        output: None"""
        if weight < 0:
            raise ValueError("Weight can't be negative")
        else:
            self.weight = round(weight, 2)
            
    def lower_amount(self, amount: int) -> None:
        """lower the amount the product amount
        
        total amount can't be negative
        param: amount
        output: none"""
        if self.amount - amount < 0:
            print(f"Maximum amount that can be removed is {self.amount}")
        if self.amount - amount > -1:
            print(f"Operation successful")
            self.amount -= amount
        
            
    def higher_amount(self, amount: int) -> None:
        """Make amount of product avalabile higher

        Args:
            amount (int): amount to be added to stock
        """
            
            
    def get_name(self) -> str:
        """Return product name.
        
        param:None
        output: self.name
        """
        return self.name

    
    def get_price(self) -> float:
        """Return product price.
        
        param:None
        output: self.price
        """
        return self.price


    def get_weight(self) -> float:
        """Return product weight.
        
        param:None
        output: self.weight
        """
        return self.weight

    def get_description(self) -> str:
        """Return product description.
        
        param:None
        output: self.name
        """
        return self.description
    
    def get_type(self) -> str:
        """Return product type.
        
        param:None
        output: self.type
        """
        return self.type
    