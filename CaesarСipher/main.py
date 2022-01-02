def read_string():
    string = input()
    return string


def length(word):
    word_length = 0
    for char in word:
        if char.isalpha():
            word_length += 1
    return word_length


def encrypt(word, word_length):
    encrypted_word = ''
    for char in word:
        if char.isalpha():
            if ord(char) + word_length in [91, 92, 93, 94, 95, 96] or ord(char) + word_length > 122:
                encrypted_word += chr(ord(char) + word_length - 26)
            else:
                encrypted_word += chr(ord(char) + word_length)
        else:
            encrypted_word += char
    return encrypted_word


def main():
    words = read_string().split()
    encrypted_string = []
    for word in words:
        word_length = length(word)
        encrypted_word = encrypt(word, word_length)
        encrypted_string.append(encrypted_word)
    print(' '.join(encrypted_string))


main()
