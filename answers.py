def revers_sentence(sentence):
    reversed_sentence = sentence[::-1].title()
    return reversed_sentence

# print(revers_sentence('Ala ma kota'))
# print(revers_sentence('Python is easy'))

def count_char(sentence, character):
    uni_sentence = sentence.lower()
    uni_character = character.lower()
    counter = 0
    for _ in uni_sentence:
        if _ == uni_character:
            counter +=1
    return counter

print(count_char('Ala ma koTA', 'a'),
      count_char("ala ma kota",'A'),
      count_char("Python is easy",'a'))


def list_filter(int_values, *args):
    temp_int_values = int_values
    for element in args:
        for number in temp_int_values:
            if number % element == 0:
                temp_int_values.remove(number)
    return temp_int_values

# print(list_filter([1,8,15,20,11], 20))
# print(list_filter([1,8,15,20,11], 20,4))
# print(list_filter([1,8,15,20,11], 2, 5, 31))

def get_random_elements(elements_list, number=1):
    for _ in range(number):

