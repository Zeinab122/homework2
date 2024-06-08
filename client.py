import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 4444))

    account_number = input("Enter your account number: ")
    client.send(account_number.encode())

    print(client.recv(1024).decode())

    while True:
        print("Options:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        option = input("Enter option: ")

        if option == '4':
            break

        client.send(option.encode())

        if option == '1':
            print(client.recv(1024).decode())
        elif option == '2' or option == '3':
            amount = input("Enter amount: ")
            client.send(amount.encode())
            print(client.recv(1024).decode())

    client.close()


if __name__ == "__main__":
    main()