from functools import wraps
from core import *

WALLETS = WalletList()

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            print('value errorr')
        except MemoryError:
            print('\nNo data')
        except KeyError:
            print('command dont exist')
    return wrapper


@input_error
def create_waste(args:list):
    name, amount, category, wallet = args[0],args[1],args[2],args[3]
    if wallet not in WALLETS.data.data:
        print('wallet no in data.data')
        return False
    print('==')
    print(WALLETS.data.data)
    print('==')

    waste_builder = WasteBuilder() \
            .set_name(name) \
            .set_amount(amount) \
            .set_category(category) \
    
    waste = waste_builder.create()
    WALLETS.data[wallet].add_waste(waste)
    wallet = WALLETS.data[wallet]
    WALLETS.save_data(wallet)
    return waste

@input_error
def create_wallet(args:list):
    name, amount = args[0],args[1]
    wallet = Wallet(name, amount)
    WALLETS.save_data(wallet)

    return wallet

@input_error
def show_wallet_spendings(args:list):
    wallet_name = args[0]
    return WALLETS.data.data[wallet_name].get_info()

@input_error
def show_wallets():
    if WALLETS.get_info() == None:
        raise MemoryError
    return WALLETS.get_info()

@input_error    
def delete_wallet(wal_name):
    WALLETS.del_wallet(wal_name)

@input_error    
def delete_spend(spend_name):
    WALLETS.data

def quit():
    print('Se u :)')
    exit()

def useful_inputs():
    r = input(': ')
    return r





