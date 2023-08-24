def is_anagram(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the lengths are different
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each character in both words
    char_count1 = {}
    char_count2 = {}

    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare the character counts
    return char_count1 == char_count2

# Get input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the words are anagrams
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams!")
else:
    print(f"{word1} and {word2} are not anagrams.")
