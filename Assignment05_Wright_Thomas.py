''''

Title: Fdn 100 Assignment 05 -- dictionaries
Dev: Thomas Wright
Date: 4/23/2018
ChangeLog: None

Description:
This program is a To-Do list that lists the task and its priority.
The program interacts with a text file. It allows the user to:
** see the current contents of the file
** Add a new item
** Remove an existing item.
** Save Data to File
** Exit Program without saving
It will present the user with the above options and utilizing dictionaries to store the pairs.

Input:
There are two forms of input:
1. The contents of Todo.txt
2. User generated input

Output:
Stores the user input to a file with a comma separating the task and its priorities.
The input file will be over-written each time to allow for ease of formatting and to aid in deleting items
The data will resemble rows
It will be easy to read into python as a csv!

'''

## -- Data -- ##

## Loading the data from file

lst_of_dicts = []

with open('Todo.txt', 'r+') as file:
    lst_values = file.readlines()
    lst_values = [i.strip() for i in lst_values]
    lst_values = [i.split(',') for i in lst_values]
    del(lst_values[0]) # bit un-necessary

for lst in lst_values:
    d = {lst[0]:lst[1]}
    lst_of_dicts.append(d)



## -- Processing -- ##

## Helper functions

def print_list(lst):
    print('')
    print( 'Your to-do list is:')
    print('Index  ' + 'Task' + ' : ' + 'Priority')
    for idx, d in enumerate(lst_of_dicts):
        print(str(idx), d)

def add_item(lst):
    while True:
        user_task = input('Enter a task name: ')
        user_priority = input('Enter the priority : ')
        d = {user_task.capitalize():user_priority}
        lst.append(d)
        user_continue = input("Enter 'y' to continue adding tasks, anything else to exit: ")
        if user_continue.lower() == 'y':
            continue
        else:
            break

def delete_index(lst):
    done = False
    while not done:
        print_list(lst)
        try:
            user_index = int(input('Enter the index of the task to delete: '))
            del[lst[user_index]]
        except:
            print('Must enter an integer that exists in the printed list.')
            continue
        while True:
            user_exit = input("Enter 'E' to exit or 'C' to continue deleting: ")
            if user_exit.lower() == 'e':
                done = True
                break
            elif user_exit.lower() == 'c':
                break
            else:
                print('Incorrect option, please select again: ')


def delete_key(lst):
    done = False
    while not done:
        print_list(lst)
        count = 0
        try:
            user_word = input('Enter the task to delete: ')
            for d in lst:
                if user_word.capitalize() in d:
                    lst.remove({user_word.capitalize():d[user_word.capitalize()]})
                    count += 1
            if count < 1:
                print('Nothing to delete')
        except:
            print('Error in input. Make sure it is a string!')
        while True:
            user_exit = input("Enter 'E' to exit or 'C' to continue deleting: ")
            if user_exit.lower() == 'e':
                done = True
                break
            elif user_exit.lower() == 'c':
                break
            else:
                print('Incorrect option, please select again: ')


def save_data(lst):
    with open('Todo.txt', 'w+') as file:
        file.write('Task' + ',' + 'Priority' + '\n')
        for d in lst:
            for key, value in d.items():
                file.write(key + ',' + value + '\n')



## -- Presentation (I/O)

## Running the program

print('Welcome to your To-Do List')
print("Let's get started!")

while True:
    print('''
    Options Menu
    
    1) Show current To-Do list
    2) Add a new Task
    3) Remove an existing Task
    4) Save Data to File
    5) Exit Program
    ''')
    user_choice = int(input('Please select a number: '))
    if user_choice == 1:
        print_list(lst_of_dicts)
    elif user_choice == 2:
        add_item(lst_of_dicts)
    elif user_choice == 3:
        print('Do you want to delete by index or name?')
        while True:
            delete_option = input('Enter I for index or N for name: ')
            if delete_option.lower() == 'i':
                delete_index(lst_of_dicts)
                break
            elif delete_option.lower() == 'n':
                delete_key(lst_of_dicts)
                break
            else:
                print('Incorrect entry.')
    elif user_choice == 4:
        save_data(lst_of_dicts)
    elif user_choice == 5:
        print('Goodbye!')
        break
    else:
        print('Incorrect entry, select a number 1-5!')
