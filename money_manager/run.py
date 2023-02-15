from core import *
from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print('done')
            return result
        except:
            raise ValueError('Command not found')
    return wrapper


@input_error
def create_waste(args:list):
    name, amount, category = args[0],args[1],args[2],
    waste = WasteBuilder() \
            .set_name(name) \
            .set_amount(amount) \
            .set_category(category) \
    
    print(waste.name)
    return waste


COMMANDS = {
    'cw' : [['name', 'amount', 'category'],[create_waste]],
}

def useful_inputs():
    r = input(': ')
    return r

@input_error
def smart_handler(command):
    argues=[]
    com = COMMANDS[command]
    for i in com[0]:
        print(f"Enter the {i}")
        arg = useful_inputs()
        argues.append(arg)
    print(com[1][0])
    com[1][0](argues)
    

def execute(handler):
    print(handler)

def main(data):
    while True:
        for command in COMMANDS:
            print(command)

        command = useful_inputs()
        smart_handler(command)

        input()


if __name__ == "__main__":
    data = FileData()
    main(data)



