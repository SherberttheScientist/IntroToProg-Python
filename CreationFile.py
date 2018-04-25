'''

Creating the input file for Assignment 05

'''

outerlst = [{'Task':'Priority'}, {'Clean House':'low'}, {'Pay Bills':'high'}]

with open('Todo.txt', 'w') as file:
    for d in outerlst:
        for key, value in d.items():
            file.write(key + ',' + value + '\n')


