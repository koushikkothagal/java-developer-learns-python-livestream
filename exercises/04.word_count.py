# Exercise 4: Word Count in a Text

# Create a Python program that asks the user to input a sentence or paragraph, 
# and then counts and displays the total number of words in that input.

# For an additional challenge:

# Count the occurrence of each word and display it.
# Ignore case while counting word occurrences 
# (for example, "The" and "the" should be counted as the same word).

paragraph = input()



split_strings = [ n for n in paragraph.split(' ') if n ]
print(f'Total number of words: {len(split_strings)}')

occurrence_count = {}

for word in split_strings:
    lower_case_word = word.lower()
    if lower_case_word in occurrence_count:
        occurrence_count[lower_case_word] = occurrence_count[lower_case_word] + 1
    else:
        occurrence_count[lower_case_word] = 1

print(occurrence_count)


