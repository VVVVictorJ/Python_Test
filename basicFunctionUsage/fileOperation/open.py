# Open the file named '1.txt' in read mode
with open('1.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file
    file_contents = file.read()
    
# Print the contents of the file
print(file_contents)

