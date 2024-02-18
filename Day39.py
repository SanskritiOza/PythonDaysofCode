from collections import Counter
import re

def most_common_words(file_path, num_words=10):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the most common words
    most_common = word_counts.most_common(num_words)

    return most_common

if __name__ == "__main__":
    file_path = 'your_text_file.txt'
    num_words = 10  # Change this to get more or fewer common words
    common_words = most_common_words(file_path, num_words)
    print("The most common words in the file are:")
    for word, count in common_words:
        print(f"{word}: {count}")
