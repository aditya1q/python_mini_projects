# you can type anything it will become password
master_password = input('Enter the password for Login: ')

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if '|' in data:
                    user, passw = data.split('|')
                    print(f"User: {user} | Password: {passw}")
                else:
                    print("entry:", data)
    except FileNotFoundError:
        print("No saved passwords found.")

def add():
    user_name = input("Enter the user name: ")
    user_password = input('Enter the password: ')

    with open('password.txt', 'a') as f:
        f.write(f'user: {user_name} , password: {user_password}' + "\n")


while True:
    mode = input(
        'Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()

    if mode == 'q':
        quit()

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue
