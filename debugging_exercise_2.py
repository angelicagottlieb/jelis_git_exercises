
def encode(text, key):
    cipher = make_cipher(key)
    print(f"We start with a code which looks like this {cipher}")

    ciphertext_chars = []
    for i in text:
        print(f"For {i} in text")
        ciphered_char = chr(65 + cipher.index(i))
        print(f"For {ciphered_char} it's equal to {chr(65 + cipher.index(i))}")
        print(ciphered_char)
        ciphertext_chars.append(ciphered_char)
        print(ciphertext_chars)
        string_to_use =  "".join(ciphertext_chars)
        print(string_to_use)
        return string_to_use 



def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"We start with a code which looks like this {cipher}")

    plaintext_chars = []
    for i in encrypted:
        print(f"For {i} in encrypted")
        plain_char = cipher[ord(i) - 65]
        print(f"We then get {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    print(cipher)
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""Running: encode("t", "secretkey")
Expected: E
Actual: {encode('t', 'secretkey')}
""")
print(f"""
Running: decode("E", "secretkey")
Expected: t
Actual: {decode('E', 'secretkey')}
""")

print(f"""
Running: make_cipher("secretkey")
Expected: not sure
Actual: {make_cipher('secretkey')}
""")

