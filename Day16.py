def count_word_frequency(sentence):
    word_frequency = {}  # Dictionary to store word frequencies

    # Split the sentence into words
    words = sentence.split()

    for word in words:
        # Remove punctuation marks if present
        word = word.strip('.,!?:"()[]{}')

        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()

        # Update the word frequency in the dictionary
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

# Example usage:
input_sentence = input("Enter a sentence: ")
result = count_word_frequency(input_sentence)

print("Word frequencies:")
for word, frequency in result.items():
    print(f"{word}: {frequency}")
