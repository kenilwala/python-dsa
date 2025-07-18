def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))
print(is_palindrome("string"))

def fibonacci(n):
    seq = [0,1]
    while len(seq)<n:
        seq.append(seq[-1]+seq[-2])
    return seq[:n]

print(fibonacci(13))

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

print(count_vowels("Kenil"))

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

print(remove_duplicates([1,2,3,4,5,6,3,1,1,2,3]))

def word_frequencies(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word]= freq.get(word,0)+1
    return freq


print(word_frequencies("apple banana apple orange banana apple"))