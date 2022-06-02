from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name: Name, num: Phone = None) -> None:
        self.name = name
        self.nums = []
        if num:
            self.nums.append(num)
            
    def add(self, new_num: Phone):
        if new_num.value not in [p.value for p in self.nums]:
            self.nums.append(new_num)
            return new_num
    
    def remove(self, num: Phone):
        for i, p in enumerate(self.nums):
            if num.value == p.value:
                return self.nums.pop(i)
        
    def edit(self, num: Phone, new_num: Phone):
        if self.remove(num):
            self.nums.append(new_num)
            return new_num


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "give me 'add' 'name' 'number'"
        except KeyError:
            return "Give me 'name' and 'phone' please"
        except ValueError:
            return "Give me 'change' 'name' 'number'"
    return wrapper


def start_bot():
    return "How can I help you?"

def exit_bot():
    return "Good bye!"

def close_bot():
    return "Good bye!"

def bye_bot():
    return "Good bye!"

data = {}

contacts = {}

ab = AddressBook()

@input_error
def input_add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    ab.add_record(rec)
    return f"Contact {args[0].title()} added"


@input_error
def input_change(*args):
    rec = ab.get(args[0])
    if rec:
        phone = Phone(args[1])
        new_phone = Phone(args[2])
        rec.edit(phone, new_phone)
    return f"Contact {args[0].title()} changed"


@input_error
def input_phone(*args):
    rec = ab.get(args[0])
    if rec:
        return rec.phones()

def input_show():
    return "\n".join([f"{v.name.value}: {v.nums} " for v in ab.values()])


COMMANDS = {
    start_bot: "hello",
    input_add: "add",
    input_phone: "phone",
    input_show: "show all",
    input_change: "change",
    exit_bot: "good bye",
    close_bot: "close",
    bye_bot: "exit"
}

def main():
    while True:
        user_input = input(">>> ")
        if user_input == '.':
            break
        for k, v in COMMANDS.items():
            if user_input.startswith(v):
                cmd, data = k, user_input[len(v):].strip().split() 
        print(cmd(*data))    


if __name__ == "__main__":
    main()
  
