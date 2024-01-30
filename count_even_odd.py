def count(word):
    vowels = {"a", "e", "i", "o", "u"}
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count

def main():
    user_input = input("Enter a word: ")

    vowel_count, consonant_count = count(user_input)

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

if __name__ == "__main__":
    main()
