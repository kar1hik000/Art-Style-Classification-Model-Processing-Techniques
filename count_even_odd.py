def count(word):
    # Define the set of vowels
    vowels = {"a", "e", "i", "o", "u"}

    # Initialize counts for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the word
    for char in word:
        # Check if the character is a vowel (ignoring case)
        if char.lower() in vowels:
            vowel_count += 1
        # Check if the character is an alphabet (to exclude numbers, symbols, etc.)
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    # Get user input for a word
    user_input = input("Enter a word: ")

    # Call the count function to get counts of vowels and consonants
    vowel_count, consonant_count = count(user_input)

    # Print the results
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
