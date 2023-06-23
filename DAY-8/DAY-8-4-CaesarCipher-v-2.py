from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, direction):
    if direction == "decode":
        shift_amount= shift_amount*(-1)
    our_text = ""
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            our_text = our_text + new_letter
        else:
            our_text = our_text+i
    print(f"The {direction} text is the {our_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # If user enters a number bigger than what we have available
    shift =shift%26
     
    caesar(plain_text=text, shift_amount=shift, direction=direction)
    reply = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if reply == "no":
        print("Goodbye!")
        break