def encrypt(string: str, num: int) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet: str = alphabet.upper()
    encrypted_str: str = ""

    for c in string:
        if c in alphabet:
            if (alphabet.find(c) + num) < 26:
                encrypted_str += alphabet[alphabet.find(c) + num]
            else:
                encrypted_str += alphabet[(alphabet.find(c) + num) - 26]
        elif c in upper_alphabet:
            if (upper_alphabet.find(c) + num) < 26:
                encrypted_str += upper_alphabet[upper_alphabet.find(c) + num]
            else:
                encrypted_str += upper_alphabet[(upper_alphabet.find(c) + num) - 26]
        else:
            encrypted_str += c

    return encrypted_str

def decrypt(string: str) -> None:
    for i in range(1, 26):
        print(f"key {i}: {encrypt(string, i)}")

def main() -> None:
    running: bool = True
    while running:
        print("1. Encrypt a string")
        print("2. Decrypt a string")
        print("3. Exit")
        user_choice: str = input("Enter the action you'd like to perform(1, 2, 3): ")

        match user_choice:
            case "1":
                user_str: str = input("Enter the string you want to encrypt: ")
                asking: bool = True
                
                while asking:
                    user_num = int(input("Enter the number you want to encrypt your string by: "))
                    if user_num > 0 and user_num < 27:
                        asking = False
                        secret_str: str = encrypt(user_str, user_num)

                        print(f"Here's your secret message: {secret_str}")
                    else:
                        print("Please enter a valid integer between 1 and 26.")
            case "2":
                user_str = input("Please enter the string you would like to decrypt: ")
                print("Here are all possible decryption keys")
                decrypt(user_str)
            case "3":
                running = False
            case _:
                print("Please enter a valid input (1, 2, 3).")

if __name__ == "__main__":
    main()
