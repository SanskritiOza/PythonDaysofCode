def capitalize_sentence(sentence):
    # Using title() method to capitalize the first letter of each word
    capitalized_sentence = sentence.title()
    return capitalized_sentence

# Example usage:
input_sentence = "hello world! this is a sample sentence."
output_sentence = capitalize_sentence(input_sentence)

print("Input Sentence:", input_sentence)
print("Capitalized Sentence:", output_sentence)
