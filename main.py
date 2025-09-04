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

def main() -> None:

    user_str: str = input("Enter the string you want to encrypt: ")

    asking: bool = True
    while asking:
        user_num = int(input("Enter the number you want to encrypt your string by: "))
        if user_num > 0 and user_num < 27:
            asking = False
        else:
            print("Please enter a valid integer between 1 and 26.")

        secret_str: str = encrypt(user_str, user_num)

    print(f"Here's your secret message: {secret_str}")

if __name__ == "__main__":
    main()