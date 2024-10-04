{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "767b40e4-73fe-400d-ba18-3973aa5cf35b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Caesar:  \n",
    "    def __init__(self, key: int = 0): \n",
    "        self._key = key\n",
    "\n",
    "    def key_get(self) -> int:\n",
    "        return self._key\n",
    "\n",
    "    def set_key(self, key: int) -> None:\n",
    "        if isinstance(key, int):\n",
    "            self._key = key\n",
    "        else:\n",
    "            raise ValueError(\"The key has to be an integer\")\n",
    "\n",
    "    def _shift_char(self, char: str, shift_amount: int) -> str:\n",
    "        if char.isalpha():\n",
    "            base = ord('a')  \n",
    "            return chr((ord(char.lower()) - base + shift_amount) % 26 + base)\n",
    "        else:\n",
    "            return chr((ord(char) + shift_amount) % 128)\n",
    "\n",
    "    def encrypt(self, plaintext: str) -> str:\n",
    "        ciphertext = \"\".join(self._shift_char(char, self._key) for char in plaintext)\n",
    "        return ciphertext\n",
    "\n",
    "    def decrypt(self, ciphertext: str) -> str:\n",
    "        plaintext = \"\".join(self._shift_char(char, -self._key) for char in ciphertext)\n",
    "        return plaintext"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "52590b49-db0d-4f84-8081-82789ca18b19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "khoor#zruog$\n",
      "hello\u001d",
      "world!\n",
      "fff\n",
      "zzz\n",
      "zzz\n"
     ]
    }
   ],
   "source": [
    "cipher = Caesar()  # Instantiate the Caesar object\n",
    "cipher.set_key(3)  # Set key to 3\n",
    "print(cipher.encrypt(\"hello WORLD!\"))  # prints “khoor zruog$”\n",
    "print(cipher.decrypt(\"KHOOR zruog$\"))  # prints “hello world!”\n",
    "\n",
    "cipher.set_key(6)  # Set key to 6\n",
    "print(cipher.encrypt(\"zzz\"))  # prints “fff”\n",
    "print(cipher.decrypt(\"FFF\"))  # prints “zzz”\n",
    "\n",
    "cipher.set_key(-6)  # Set key to -6 (negative keys)\n",
    "print(cipher.encrypt(\"FFF\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146ad0db-6958-465b-b2db-a248a65991bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
