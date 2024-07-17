import random


def change_upper(letters):
    return [x.upper()for x in letters]


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

generated_password = []

def clear_list():
    generated_password.clear()

def generate_pass():
    letter_len = random.randint(8,10)
    symbols_len = random.randint(2,4)
    numbers_len = random.randint(2,4)

    # for letter in letters:
    #     random_letters = random.choices(letters, k=letter_len)

    # for symbol in symbols:
    #     random_symbols = random.choices(symbols, k=symbols_len)

    # for number in numbers:
    #     random_numbers = random.choices(numbers, k=numbers_len)

    password_letters = [random.choice(letters) for _ in range(letter_len)]
    password_symbols = [random.choice(symbols) for _ in range(symbols_len)]
    password_numbers = [random.choice(numbers) for _ in range(numbers_len)]

    generated_password.extend(password_letters)
    generated_password.extend(password_symbols)
    generated_password.extend(password_numbers)

    new_pw = list(generated_password) 
    
    random.shuffle(new_pw)
 
    random_password = ''.join(map(str, new_pw))
    clear_list()
    # print(generated_password)
    # print(random_password)
    
 
    return random_password


generate_pass()

