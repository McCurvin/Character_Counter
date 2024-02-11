
def McCurvin(user_input):
    special = 0
    alphabet = 0
    consonant = 0
    vowel = 0
    digits = 0
    odd = 0
    even = 0

    for mixedSignals in user_input:
        if mixedSignals.isalpha():
            alphabet += 1
            if mixedSignals.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                consonant += 1
        elif mixedSignals.isdigit():
            digits += 1
            if int(mixedSignals) % 2 == 0:
                even += 1
            else:
                odd += 1
        else:
            special += 1
    return special, alphabet, consonant, vowel, digits, odd, even

if __name__ == "__main__":
    while True:
        user_input = input("Enter mixed characters here: ")
        if len(user_input.split()) > 0:
            break
        else:
            print("Enter a non-empty string please. Thank you very much xoxo arigato ilysm!")

    verySpecial, veryAlphaMale, veryConsonant, veryVowel, veryDigit, veryOdd, veryEven = McCurvin(user_input)
    print(f"Total special characters\t: {verySpecial}")
    print(f"Total alphabets\t\t\t\t: {veryAlphaMale}")
    print(f"Total consonants\t\t\t: {veryConsonant}")
    print(f"Total vowels\t\t\t\t: {veryVowel}")
    print(f"Total number of digits\t\t: {veryDigit}")
    print(f"Total odd numbers\t\t\t: {veryOdd}")
    print(f"Total even numbers\t\t\t: {veryEven}")
