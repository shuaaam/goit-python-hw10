from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value.name()


class Name(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Phone(Field):
    def __init__(self, *args):
        self.items = []
        super().__init__(*args)


class Record:

    def __init__(self, name: Name, nums: Phone) -> None:
        self.name = name
        self.nums = nums

    def edit(self, num: Phone, new_num: Phone):
        if self.remove_record(num):
            self.nums.append(new_num)
            return new_num

    def remove(self, num: Phone):
        for i in enumerate(self.nums):
            if num.value == num.value:
                return self.nums.pop(i)

    def add(self, new_num: Phone):
        if self.add_record(new_num):
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

@input_error
def input_add(*args):
    data.update({args[0]: args[1]})
    return f"Contact {args[0].title()} added"


@input_error
def input_change(*args):
    data[args[0]] = args[1]
    return f"Contact {args[0].title()} changed"


@input_error
def input_phone(*args):
    return data[args[0]]

def input_show():
    for k, v in data.items():
        _ = k.title() + ' ' + str(v)
        contacts.append(_)
    return "\n".join([f"{k}: {v} " for k, v in contacts.items()])


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
        for k, v in COMMANDS.items():
            if v == user_input:
                print(k())
            if user_input == '.':
                break
            user_input = user_input.lower()
            if user_input in ['good bye', 'exit', 'close']:
                False
            cmd = user_input
            if cmd[0] == 'add':
                contacts.extend(cmd)
                print(input_add())
                contacts.clear()
            if cmd[0] == 'change':
                contacts.extend(cmd)
                print(input_change())
                contacts.clear()
            if cmd[0] == 'phone':
                contacts.extend(cmd)
                print(input_phone(), end='\n')
                contacts.clear()


if __name__ == "__main__":
    main()

ab = AddressBook()
name = Name("Bill")
phone = Phone("39887")
rec = Record(name, phone)
ab.add_record(rec)
print(ab)
phone2 = Phone("12554")
rec.change_phone(phone, phone2)
phone3 = Phone("099776")
rec.add_phone(phone3)
print(ab)
