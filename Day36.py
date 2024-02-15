def are_anagrams(str1, str2):
    # Removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
