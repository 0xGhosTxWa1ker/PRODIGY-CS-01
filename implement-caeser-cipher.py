def caesar_cipher(text, shift, mode):
    result = ""

    # Adjust Shift Value For Decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse The Text
    for char in text:
        # Encrypt Or Decrypt Uppercase Characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt Or Decrypt Lowercase Characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep Other Characters Unchanged
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Enter 'encrypt' To Encrypt Or 'decrypt' To Decrypt: ").lower()
    message = input("Enter Your Message: ")
    shift = int(input("Enter The Shift Value (integer): "))

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid Mode Selected!")
    else:
        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

