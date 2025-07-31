
# File Read & Write Challenge

# Step 1: Read from original file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 3: Write to new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File successfully read, modified, and written to 'output.txt'.")



# Error Handling Lab

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Content ---\n")
        print(content)
except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"❌ Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"❌ Unexpected error occurred: {e}")
