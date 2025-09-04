def main() -> None:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet: str = alphabet.upper()
    encrypted_str: str = ""

    user_str: str = input("Enter the string you want to encrypt: ")

    asking: bool = True
    while asking:
        user_num = int(input("Enter the number you want to encrypt your string by: "))
        if user_num > 0 and user_num < 27:
            asking = False
        else:
            print("Please enter a valid integer between 1 and 26.")

    for c in user_str:
        if c in alphabet:
            if (alphabet.find(c) + user_num) < 26:
                encrypted_str += alphabet[alphabet.find(c) + user_num]
            else:
                encrypted_str += alphabet[(alphabet.find(c) + user_num) - 26]
        elif c in upper_alphabet:
            if (upper_alphabet.find(c) + user_num) < 26:
                encrypted_str += upper_alphabet[upper_alphabet.find(c) + user_num]
            else:
                encrypted_str += upper_alphabet[(upper_alphabet.find(c) + user_num) - 26]
        else:
            encrypted_str += c

    print(f"Here's your secret message: {encrypted_str}")

if __name__ == "__main__":
    main()