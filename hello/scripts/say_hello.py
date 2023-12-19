from colorama import Fore, Style


def say_hello():
    message = f"{Fore.RED}Hello!{Style.RESET_ALL}"
    print(message)


if __name__ == "__main__":
    say_hello()


def main():
    print("Hello!")


if __name__ == '__main__':
    main()
