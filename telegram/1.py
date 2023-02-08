def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count

word_list = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'
print(count_letter(word_list, letter))

