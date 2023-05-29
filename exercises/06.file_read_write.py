# Writing and Reading from a File

# Write a Python program that allows users to write their diary entries, and save them to a file named diary.txt. Each entry should have a timestamp attached to it to show when the entry was made. The program should also allow users to read all the entries from the file.

# This will help you understand how to work with files, which is a common task in many real-world programming situations.

import os.path as path
import json
import sys
import time

def read_diary_entry(file_name: str):  
    with open(file_name, encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return { 'entries': []}


file_name = ''
while not path.isfile(file_name):
    print('Input diary file name ')
    file_name = input()

diary_contents = read_diary_entry(file_name)


menu_choice = '0'
while menu_choice != 3:
    print("""
    Choose the operation:
    1. Print all diary contents
    2. Make a new diary entry
    3. Exit
    """)

    menu_choice = input()
    
    match menu_choice:
        case '1':
            contents = read_diary_entry(file_name)
            print('**** Entries ****')
            [print(entry['entry_text']) for entry in contents['entries']]
        case '2':
            print('Enter new diary entry')
            entry_text = input()
            new_entry = {
                'entry_text': entry_text,
                'timestamp': time.time()
            }

            diary_contents['entries'].append(new_entry)
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(diary_contents, file)
        case '3':
            sys.exit()
        case _:
            continue



