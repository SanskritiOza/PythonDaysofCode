import re

def words_starting_with_vowel(sentence):
    # Define a regular expression pattern to match words starting with a vowel
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    
    # Find all matches in the sentence
    matches = re.findall(pattern, sentence)
    
    return matches

# Example usage:
sentence = "An example sentence to test the function that finds words starting with vowels."
vowel_words = words_starting_with_vowel(sentence)
print(vowel_words)
