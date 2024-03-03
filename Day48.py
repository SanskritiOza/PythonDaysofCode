import nltk
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def replace_with_synonyms(text):
    tokens = nltk.word_tokenize(text)
    replaced_tokens = []
    for token in tokens:
        synonyms = get_synonyms(token)
        if synonyms:
            replaced_tokens.append(synonyms.pop())  # Replace with the first synonym
        else:
            replaced_tokens.append(token)
    return ' '.join(replaced_tokens)

def main():
    text = "I love to eat pizza and drink soda."
    replaced_text = replace_with_synonyms(text)
    print("Original text:", text)
    print("Text with synonyms replaced:", replaced_text)

if __name__ == "__main__":
    main()
