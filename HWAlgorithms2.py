#Level1
#Task1

def reverse_integer(n: int):
    number  = str(n)
    if number[0] == '-':
        return int("-" + number[1::-1])
    else:
        return int(number[0::-1])

#Task 2
def are_anagrams(s1: str, s2: str):
    if len(s1) == len(s2):
        if sorted(s1.lower()) == sorted(s2.lower()):
            return True
    return False

print(are_anagrams('race', 'care'))
print(are_anagrams('hEArt', 'earth'))
print(are_anagrams('rattle','battle'))

#Task3

def reverse_words(sentence: str):
# Split the sentence into individual words using the .split() method
    sentence_list = sentence.split()
# Create an empty list to store the reversed versions of words
    reversed_list = []
# Iterate through each word in the list of words
    for word in sentence_list:
# Reverse each word using string slicing with a step of -1
        word_reversed = word[::-1]
# Append the reversed word to the list of reversed words
        reversed_list.append(word_reversed)
# Join (.join) the reversed words back together into a single string, separated by spaces
    reversed_sentence = ' '.join(reversed_list)
# Return the final reversed sentence
    return reversed_sentence

print(reverse_words('Hello World'))
print(reverse_words('mistertwister'))

# s = 'ABCDE'
#
# print(s[:1]) #A
# print(s[1:]) #BCDE
# print(s[::2]) #ACE
# print(s[2:]) #CDE
# print(s[-2:]) # DE
# print(s[2::-1]) #CBA
# print(s[-1:]) #E
# print(s[:0:-1]) #EDCB

#Task4

def repeat_digits(s: str):
    result = ""  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        current_num = int(char)  # Convert the character to an integer
        repeated_char= char * current_num  # Repeat the character based on its integer value
        result = result + repeated_char
    return result  # Return the final result string

print(repeat_digits('312'))
print(repeat_digits('102'))

#Task5

def shortcut(s: str):
    result = ""
    vowels = ['a','e','i','o','u']
    for char in s:
        if char not in vowels:
            result = result + char
    return result

print(shortcut('hello'))
print(shortcut('goodbye'))