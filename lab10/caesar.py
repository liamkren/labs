def shift_character(char, shift):
    if 'a' <= char <= 'z':
        new_position = ord(char) + shift
        if new_position > ord('z'):
            new_position = ord('a') + (new_position - ord('z') - 1)
        elif new_position < ord('a'):
            new_position = ord('z') - (ord('a') - new_position - 1)
        return chr(new_position)

    elif 'A' <= char <= 'Z':
        new_position = ord(char) + shift
        if new_position > ord('Z'):
            new_position = ord('A') + (new_position - ord('Z') - 1)
        elif new_position < ord('A'):
            new_position = ord('Z') - (ord('A') - new_position - 1)
        return chr(new_position)

    else:
        new_position = ord(char) + shift
        if new_position > 127:
            new_position = new_position - 128
        elif new_position < 0:
            new_position = new_position + 128
        return chr(new_position)

def caesar_cipher(text, shift):
    return ''.join(shift_character(char, shift) for char in text)

def encrypt(plaintext, key):
    encrypted = caesar_cipher(plaintext, key)
    print(f"Encrypting with key {key}:")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {encrypted}")
    return encrypted

def decrypt(ciphertext, key):
    decrypted = caesar_cipher(ciphertext, -key)
    print(f"Decrypting with key {key}:")
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext: {decrypted}")
    return decrypted

if __name__ == "__main__":
    key = 3
    plaintext = "hello WORLD!"
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    key = 30
    plaintext = "Caesar Cipher!"
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    key = -3
    plaintext = "Python Programming"
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    key = 10
    plaintext = "12345!@#$%"
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)
