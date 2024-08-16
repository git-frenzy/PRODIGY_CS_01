def caesar_encrypt(text, shift):
    """
    Encrypts the text using Caesar Cipher with the given shift value.
    
    Parameters:
    text (str): The text to be encrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_decrypt(text, shift):
    """
    Decrypts the text using Caesar Cipher with the given shift value.
    
    Parameters:
    text (str): The text to be decrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The decrypted text.
    """
    return caesar_encrypt(text, -shift)


def main():
    """
    Main function to run the Caesar Cipher program.
    """
    print("Caesar Cipher Encryption and Decryption")
    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, (Q)uit: ").upper()
        
        if choice == 'Q':
            break
        elif choice in ('E', 'D'):
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            
            if choice == 'E':
                result = caesar_encrypt(text, shift)
                print(f"Encrypted Message: {result}")
            else:
                result = caesar_decrypt(text, shift)
                print(f"Decrypted Message: {result}")
        else:
            print("Invalid option. Please choose 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
