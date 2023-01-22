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
            raise ValueError("for removing money use method {remove_money(amount)}")
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
