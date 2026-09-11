"""
HIT137 Assignment 2 - Question 1
File: cipher.py

Reads raw_text.txt, encrypts it using two non-negative integer shifts,
decrypts the encrypted file, and verifies that the decrypted text matches
the original text.
"""


def shift_in_range(ch: str, amount: int, first: str, last: str) -> str:
    """Shift ch cyclically inside the inclusive character range first..last."""
    start = ord(first)
    size = ord(last) - start + 1
    return chr((ord(ch) - start + amount) % size + start)


def encrypt_character(ch: str, shift1: int, shift2: int) -> str:
    """Encrypt one character according to the assignment rules."""
    if "a" <= ch <= "n":
        return shift_in_range(ch, shift1 * shift2, "a", "n")

    if "o" <= ch <= "z":
        return shift_in_range(ch, -(shift1 + shift2), "o", "z")

    if "A" <= ch <= "M":
        return shift_in_range(ch, -shift1, "A", "M")

    if "N" <= ch <= "Z":
        return shift_in_range(ch, shift2 ** 2, "N", "Z")

    if "0" <= ch <= "9":
        return shift_in_range(ch, shift1 - shift2, "0", "9")

    # Spaces, tabs, newlines, punctuation and symbols stay unchanged.
    return ch


def decrypt_character(ch: str, shift1: int, shift2: int) -> str:
    """Reverse the encryption rule for one character."""
    if "a" <= ch <= "n":
        return shift_in_range(ch, -(shift1 * shift2), "a", "n")

    if "o" <= ch <= "z":
        return shift_in_range(ch, shift1 + shift2, "o", "z")

    if "A" <= ch <= "M":
        return shift_in_range(ch, shift1, "A", "M")

    if "N" <= ch <= "Z":
        return shift_in_range(ch, -(shift2 ** 2), "N", "Z")

    if "0" <= ch <= "9":
        return shift_in_range(ch, -(shift1 - shift2), "0", "9")

    return ch


def encrypt_file(
    shift1: int,
    shift2: int,
    input_path: str,
    output_path: str
) -> None:
    """Read input_path and write its encrypted contents to output_path."""
    with open(input_path, "r", encoding="utf-8") as infile:
        text = infile.read()

    encrypted_text = "".join(
        encrypt_character(ch, shift1, shift2)
        for ch in text
    )

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(encrypted_text)


def decrypt_file(
    shift1: int,
    shift2: int,
    input_path: str,
    output_path: str
) -> None:
    """Read input_path and write its decrypted contents to output_path."""
    with open(input_path, "r", encoding="utf-8") as infile:
        text = infile.read()

    decrypted_text = "".join(
        decrypt_character(ch, shift1, shift2)
        for ch in text
    )

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(decrypted_text)


def verify_files(original_path: str, decrypted_path: str) -> bool:
    """Compare two files and print whether decryption was successful."""
    with open(original_path, "r", encoding="utf-8") as original_file:
        original_text = original_file.read()

    with open(decrypted_path, "r", encoding="utf-8") as decrypted_file:
        decrypted_text = decrypted_file.read()

    success = original_text == decrypted_text

    if success:
        print("Decryption successful: files match.")
    else:
        print("Decryption failed: files do not match.")

    return success


def read_non_negative_integer(prompt: str) -> int:
    """Keep prompting until a non-negative integer is entered."""
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value

        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    """Run encryption, decryption and verification."""
    shift1 = read_non_negative_integer("Enter shift1: ")
    shift2 = read_non_negative_integer("Enter shift2: ")

    encrypt_file(
        shift1,
        shift2,
        "raw_text.txt",
        "encrypted_text.txt"
    )

    decrypt_file(
        shift1,
        shift2,
        "encrypted_text.txt",
        "decrypted_text.txt"
    )

    verify_files(
        "raw_text.txt",
        "decrypted_text.txt"
    )


if __name__ == "__main__":
    main()
