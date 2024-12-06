with open('learning_python.txt', 'r') as file:
    for line in file:
        modified_line = line.replace('Python', 'C++')
        print(modified_line)