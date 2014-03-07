def in_bisect(word_list, word):
     i = bisect_left(word_list, word)
     if i != len(word_list) and word_list[i] == word:
        return True
     else:
        return False