from functools import wraps
from core import *
from logger import get_logger
import logging

logger = get_logger(__name__)


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
        except AttributeError:
            print('Dont exist')
    return wrapper


@input_error
def wal_by_name(wal_name):
    logger.log(level=logging.ERROR, msg=f"{wal_by_name.__name__}, {wal_name}")
    wallet = WALLETS.data[wal_name]
    return wallet


# @input_error
def create_waste(args:list):
    logger.log(level=logging.ERROR, msg=f"{create_waste.__name__}, {args}")
    name, amount, category, wallet = args[0],args[1],args[2],args[3]
    if wallet not in WALLETS.data.data:
        raise AttributeError

    waste_builder = WasteBuilder() \
            .set_name(name) \
            .set_amount(amount) \
            .set_category(category) \
    
    waste = waste_builder.create()
    WALLETS.data[wallet].add_waste(waste)
    wallet = wal_by_name(wallet)
    WALLETS.save_data(wallet)
    return waste


@input_error
def create_wallet(args:list):
    logger.log(level=logging.ERROR, msg=f"{create_wallet.__name__}, {args}")
    name, amount = args[0],args[1]
    wallet = Wallet(name, amount)
    WALLETS.save_data(wallet)

    return wallet


@input_error
def show_wallet_spendings(args:list):
    logger.log(level=logging.ERROR, msg=f"{show_wallet_spendings.__name__}, {args}")
    wallet_name = args[0]
    return WALLETS.data.data[wallet_name].get_info()


@input_error
def show_wallets():
    logger.log(level=logging.ERROR, msg=f"{show_wallets.__name__}")
    if WALLETS.data.data == {}:
        raise MemoryError
    return WALLETS.get_info()


@input_error    
def delete_wallet(args:list):
    logger.log(level=logging.ERROR, msg=f"{delete_wallet.__name__}, {args}")
    wal_name = args[0]
    WALLETS.del_data(wal_name)
    WALLETS.save_data(None)
    return True


@input_error    
def delete_spend(args:list):
    logger.log(level=logging.ERROR, msg=f"{delete_spend.__name__}, {args}")
    wallet = wal_by_name(args[0])
    wallet.delete_waste(args[1])
    WALLETS.save_data(wallet)
    return True


def quit():
    print('Se u :)')
    exit()


def useful_inputs() -> str:
    r = str(input(': '))
    return r





