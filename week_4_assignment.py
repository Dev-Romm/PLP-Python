fname = input("Enter the file name: ")
new_fname = input("Enter the new file name to write the modified content: ")

try:
    with open(fname, 'r') as file:
        data = file.read()
        print(data)
        modified_data = data.replace(' ', '__')
    with open(new_fname, 'w') as new_file:
        new_file.write(modified_data)
        print(f"Modified content written to '{new_fname}' successfully.")
except FileNotFoundError:
    print(f"Error: The file '{fname}' was not found.")

