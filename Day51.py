def count_word_occurrences(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?").lower()
                # Count the occurrences of each word
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    filename = 'sample.txt'  # Change to your file name
    word_count = count_word_occurrences(filename)

    # Print the word count
    print("Word Count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
