alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again = "yes"
while go_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    if direction == "encode":
        def encrypt(original_text, shift_amount):
            encoded_message = ""
            for smth in original_text:
                if smth == " ":
                    encoded_message += " "
                elif smth in alphabet:
                    position = alphabet.index(smth)
                    new_position = (position + shift_amount) % len(alphabet)
                    encoded_message += alphabet[new_position]
                else:
                    encoded_message += smth  # Keep symbols unchanged
            print(f"Your encoded message is: {encoded_message}")

        encrypt(text, shift)

    elif direction == "decode":
        def decrypt(original_text, shift_amount):
            decoded_message = ""
            for smth in original_text:
                if smth == " ":
                    decoded_message += " "
                elif smth in alphabet:
                    position = alphabet.index(smth)
                    new_position = (position - shift_amount) % len(alphabet)
                    decoded_message += alphabet[new_position]
                else:
                    decoded_message += smth  # Keep symbols unchanged
            print(f"Your decoded message is: {decoded_message}")

        decrypt(text, shift)
    else:
        print("Invalid direction. Please type 'encode' or 'decode'.")

    go_again = input("Do you want to go again? Type 'yes' or 'no': ").lower()
    if go_again == "no":
        print("Goodbye!")
        break