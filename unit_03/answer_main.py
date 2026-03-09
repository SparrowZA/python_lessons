from answers import (random_password_generator,
                    check_password,
                    generate_strong_password,
                    caesar_cipher,
                    text_search
                    )
from TextExample import ChapterOne


if __name__ == "__main__":
    # 1. Random Password
    print("-----Exercise #01 ")
    password = random_password_generator()
    print(f"Randomly generated password: {password}")

    # 2. Check Password
    is_strong: bool = check_password("Test1234")
    print("-----Exercise #02")
    print(f"Is the password strong? {is_strong}")

    # 3. Generate Strong Password
    password = generate_strong_password()
    print("-----Exercise #03")
    print(f"Generated strong password: {password}")

    # 4. Caesar Cipher
    print("-----Exercise #04")
    text: str = "AaZzDdYy"
    encrypted_text = caesar_cipher(text, 1)
    print(f"original text: {text}")
    print(encrypted_text)

    # 5. Text Search
    print("-----Exercise #05")
    word_count: int = text_search(ChapterOne, "Lara")
    print(f"Lara appears {word_count} times in the text.")
