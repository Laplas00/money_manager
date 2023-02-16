from core import *
from functions import *



COMMANDS = {
    'create waste' : [['name','amount','category', 'wallet'],create_waste],
    'create wallet' : [['name','amount'],create_wallet],
    'sh wal spends' : [['wallet name'],show_wallet_spendings],
    'delete wallet' : [['wallet name'],delete_wallet],
    'delete spend' : [['spend name'],delete_spend],
    
}
NO_INP_COM = {
    'show wallets' : show_wallets,
    'exit' : quit,
}

# waste dont saving in data.txt

@input_error
def handler(command):
    argues=[]
    if command in COMMANDS:
        for i in COMMANDS[command][0]:
            print(i)
            inp = useful_inputs()
            argues.append(inp)
        com = COMMANDS[command][1]
        return com(argues)
    return NO_INP_COM[command]()
    
    

def main():
    print('___________________')
    while True:
        for command in COMMANDS:
            print(command)
        for command in NO_INP_COM:
            print(command)

        command = useful_inputs()
        handler(command)
        print("_______________")


if __name__ == "__main__":
    main()



