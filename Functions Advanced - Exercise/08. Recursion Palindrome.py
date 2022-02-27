def palindrome(word, index):
    second_index = len(word) - 1 - index
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] == word[second_index]:
        return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
