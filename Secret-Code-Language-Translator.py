import string
import random

def generate_random_chars(length):
    """Generate a random string of given length using ASCII letters."""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

def encode_message(message, char_len):
    """Encodes the message using the secret code logic."""
    words = message.split(" ")
    encoded_words = []
    
    for word in words:
        if len(word) >= 3:
            extra_prefix = generate_random_chars(char_len)
            extra_suffix = generate_random_chars(char_len)
            new_word = extra_prefix + word[1:] + word[0] + extra_suffix
            encoded_words.append(new_word)
        else:
            encoded_words.append(word[::-1])  # Reverse short words
            
    return " ".join(encoded_words)

def decode_message(message, char_len):
    """Decodes the message back to its original form."""
    words = message.split(" ")
    decoded_words = []
    
    for word in words:
        if len(word) >= 3 + 2 * char_len:
            stripped_word = word[char_len:-char_len]  # Remove added characters
            original_word = stripped_word[-1] + stripped_word[:-1]  # Shift back the first letter
            decoded_words.append(original_word)
        else:
            decoded_words.append(word[::-1])  # Reverse short words
    
    return " ".join(decoded_words)

print("\n✨ Welcome to Secret Code Language Translator ✨\n")

while True:
    user_mess = input("Enter the message (or type 'exit' to quit):\n").strip()
    if user_mess.lower() == "exit":
        print("Goodbye! 👋")
        break  # Exit the loop

    user_answer = input('Do you want to "Encode" or "Decode" the message? (Type "exit" to quit):\n').strip().lower()
    if user_answer.lower() == "exit":
        print("Goodbye! 👋")
        break
    
    if user_answer not in ["encode", "decode"]:
        print("❌ Invalid choice! Please enter 'Encode' or 'Decode'.\n")
        continue  # Restart the loop

    while True:
        try:
            char_len = int(input("Enter the number of extra characters to add/remove (e.g., 3):\n").strip())
            if char_len < 1:
                print("❌ Please enter a positive number.\n")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

    if user_answer == "encode":
        encoded_text = encode_message(user_mess, char_len)
        print(f"\n✅ The encoded message is:\n{encoded_text}\n")
    
    elif user_answer == "decode":
        decoded_text = decode_message(user_mess, char_len)
        print(f"\n✅ The decoded message is:\n{decoded_text}\n")
