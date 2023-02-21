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

    @abstractmethod
    def del_data(self):
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
            print(f'| - {i} : {self.data[i].balance}')

    def del_data(self, key):
        del self.data[key]


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
        self.balance = float(balance)
        self.data = {}
        
    def add_waste(self, waste:Waste):
        self.balance -= float(waste.amount)
        if str(date.today()) in self.data:
            self.data[str(date.today())][waste.name] = waste
        else:    
            self.data[str(date.today())] = {waste.name : waste}
    
    def get_info(self):
        for i in self.data:
            print('|_\n|',i)
            for di in self.data[i]:
                print('|{:<10}|{:^10}|{:>10}|'.format(di,self.data[i][di].amount,self.data[i][di].category  ) )

    def delete_waste(self, waste_name):
        for date in self.data:
            for waste in self.data[date]:
                if waste == waste_name:
                    self.balance += self.data[date][waste].amount
                    del self.data[date][waste]
                    return True
                continue
                

class WalletList(Data):
    def __init__(self):
        self.data = FileData()
        
    def save_data(self, wallet):
        if wallet == None:
            self.data.save_data()
            return True
        self.data.data[wallet.wallet_name] = wallet
        self.data.save_data()
        
    def get_info(self):
        self.data.get_info()

    def del_data(self, key):
        self.data.del_data(key)


        
        









    


