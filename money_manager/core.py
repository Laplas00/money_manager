from abc import abstractmethod, ABC
from functools import wraps
from collections import UserDict
import pickle
from datetime import date

print(date.today().weekday())

class Data(ABC):
    """
    My little abstract method 
    I dont fully understand why i need to use it
    but i want to practise with it, ohh..
    """
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class FileData(Data, UserDict):
    def get_data(self):
        try:
            with open('data.txt', 'rb') as file:
                self.data = pickle.load(file)
        except:
            self.data = {}
        
    def save_data(self):
        with open('data.txt', 'wb') as file:
            self.data = pickle.dump(self.data, file)

    def get_info(self):
        return self.data


class Waste:
    def __init__(self):
        self.name = None
        self.category = None
        self.amount = None
    
    def setName(self, name):
        self.name = name

    def setCategory(self, category):
        self.category = category
    
    def setAmount(self, amount):
        self.amount = amount


class WasteBuilder:
    """My improvise builder"""
    def __init__(self):
        self.waste = Waste()

    def set_name(self, name):
        self.waste.setName(name)
        return self

    def set_category(self, category):
        self.waste.setCategory(category)
        return self
    
    def set_amount(self, amount):
        self.waste.setAmount(amount)
        return self

    def create(self):
        return self.waste


class Wallet:
    def __init__(self, wallet_name:str, balance: float):
        self.wallet_name = wallet_name
        self.balance = balance
        
    def add_waste(self, data:dict, waste:Waste):
        if data.data[date.today()] in data.data:
            data.data[date.today()].append(waste)
        else:
            data.data[date.today()] = [waste]

    def get_info(self, data):
        for i in data.data:
            print(i)
    

    


