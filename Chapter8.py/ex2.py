def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        print letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    print chr(i)


def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    print res


rotate_word("banana", 12)