def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError as e:
            print(f'Give me name and phone please. {e}')
        except KeyError as e:
            print(f'Wrong user name. {e}')
        except ValueError as e:
            print(f"Phone number should be digit {e}")
    return inner

list_contact = {}

@input_error
def add_handler(user_inp):
    list_inp = user_inp.split()
    if not list_inp[2].isdigit():
        raise ValueError
    list_contact[list_inp[1].capitalize()] = list_inp[2]

@input_error
def change_handler(user_inp):
    list_inp = user_inp.split()
    if list_contact[list_inp[1].capitalize()]:
        list_contact[list_inp[1].capitalize()] = list_inp[2]

@input_error
def phone_handler(user_inp):
    list_inp = user_inp.split()
    user_name = list_inp[1].capitalize()
    user_phone = list_contact[list_inp[1].capitalize()]
    print(f'Contact {user_name} number is {user_phone}')

@input_error
def show_all_handler(user_inp):
    if not list_contact:
        print('You list contact is empty')
    else:
        print(list_contact)

def main():
    while True:
        user_inp = input('Enter contact details: ').lower().strip()
        user_exit_list = ['good bye', 'close', 'exit', '.']
        if user_inp in user_exit_list:
            print('Good bye!')
            break
        elif user_inp == 'hello':
            print('How can I help you?')
            continue
        elif 'add' in user_inp:
            add_handler(user_inp)
        elif 'change' in user_inp:
            change_handler(user_inp)
        elif 'phone' in user_inp:
            phone_handler(user_inp)
        elif 'show all' in user_inp:
            show_all_handler(user_inp)
        else:
            continue

if __name__== "__main__":
    main()