import string

def letter_counter(letter):
    vowel_words = ['a','e','i','o','u','A','E','I','O','U']
    consonants = [ch for ch in string.ascii_letters if ch not in vowel_words]
    numbers = [str(i) for i in range(10)]

    count_vowel = 0
    count_consonant = 0
    count_space = 0
    count_number = 0

    for i in letter:
        if i in vowel_words:
            count_vowel+=1
        elif i in consonants:
            count_consonant+=1
        elif i in numbers:
            count_number+=1
        elif i == " ":
            count_space+=1
    
    return count_vowel,count_consonant,count_number,count_space