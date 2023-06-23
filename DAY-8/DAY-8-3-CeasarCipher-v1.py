alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text = cipher_text + new_letter
    print(f"The encoded text is the {cipher_text}")

def decrypt (cipher_text, shift_amount):
    decrypt_text = ""
    for i in cipher_text:
        position = alphabet.index(i)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypt_text = decrypt_text + new_letter
    print(f"The decoded text is the {decrypt_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Unknown input")
        
