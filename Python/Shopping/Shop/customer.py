"""Class customer."""

from product import Product



class Customer:
    """Class customer"""
    
    
    def __init__(self, name: str, money: float, subscription: bool=False) -> None:
        """Constructor for class Customer.
        
        param: name
        param: money
        param: subscriptipn"""
        self.name = name
        self.add_money(money)
        self.subscription = subscription
        self.shoppingcart = list[Product]
        
    def __repr__(self) -> str:
        return f"Name: {self.name}, money: {self.get_money}, subscription: {self.get_subscription}"
        
        
    def subscribe(self) -> None:
        """Turn subscription on.
        
        raise ValueError if subscription is already turned on
        
        param: None
        output: None"""
        if self.subscribe is True:
            raise ValueError("Subscirption already is already turned on")
        else:
            self.subscribe = True
            
            
    def add_cart(self, item: Product, amount: int) -> None:
        """add item to shopping cart
        
        if item already in a shopping cart then increase the amount of the item in shopping cart
        
        param: item
        param: item
        output: None"""
        found = False
        for product in self.shoppingcart:
            if product.get_name() == item.name:
                product.amount += amount
                found = True
                break
        if found is False:
            item
            self.shoppingcart.append(item)
        
            
            
    
    
    def total_cost(self) -> float:
        """Get sum of all the """
        solution = 0
        
            
            
    def unsubscribe(self) -> None:
        """Turn subscription off
        
        raise ValueError if subscription is already turned on
        
        param: None
        output: None"""
        if self.subscribe is False:
            raise ValueError("Subscirpion is already turned off")
        
    def add_money(self, amount: float) -> None:
        """Add money to customer.
        
        raise ValueError if money added is negative.
        
        param: amount
        output: None"""
        if amount < 0:
            raise ValueError("for removing money use method <remove_money(amount)>")
        else:
            self.money += amount
            
    def remove_money(self, amount: float) -> None:
        """Remove money from the customer.
        
        raise ValueError if money removed is negative
        
        param: amount
        output: None"""
        if amount < 0:
            raise ValueError("for adding money use method {add_money(amount)}")
        else:
            self.money -= amount
        
            
    def get_money(self) -> float:
        """Return the amount of money customer has
        
        param: None
        output: float
        """
        return round(self.money, 2)
    
    def get_subscription(self) -> bool:
        """Return if subscription is turned off or on.
        
        param: None
        output: float"""
        return self.subscription
    
    def get_shopping_cart(self) -> list:
        """Return shopping cart of the person
        
        param: None
        output: list"""
        return self.shoppingcart
