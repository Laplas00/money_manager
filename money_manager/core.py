from abc import abstractmethod, ABC
from collections import UserDict
import pickle
from datetime import date


class Data(ABC):
    """
    My little abstract method 
    I dont fully understand why i need to use it
    but i want to practise with it, ohh..
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class FileData(Data, UserDict):
    def __init__(self):
        try:
            with open('data.txt', 'rb') as file:
                self.data = pickle.load(file)
                print('data connected')
        except:
            print('data created')
            self.data = {}
        
    def save_data(self):
        with open('data.txt', 'wb') as file:
            pickle.dump(self.data, file)

    def get_info(self):
        for i in self.data:
            print('[ - ', i)


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
        self.data = {}
        
    def add_waste(self, waste:Waste):
        if str(date.today()) in self.data:
            self.data[str(date.today())][waste.name] = {waste.amount, waste.category}
            print('i think ok')
        else:
            self.data[str(date.today())] = {}
            self.data[str(date.today())][waste.name] = {waste.amount : waste.category}
            print('else')

    def get_info(self):
        print(self.data)


class WalletList(Data):
    def __init__(self):
        self.data = FileData()
        
    def save_data(self, wallet:Wallet):
        self.data.data[wallet.wallet_name] = wallet
        self.data.save_data()
        
    def get_info(self):
        self.data.get_info()

    def del_wallet(self, wallet_name):

        print(self.data)
        print(self.data.data)
        # how is it happpened
        print(self.data == self.data.data)
        del self.data.data[wallet_name]

        
        









    


