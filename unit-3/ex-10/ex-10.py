import re

# Create a text file
with open("data.txt", "w") as f:
    f.write("Name: Vishwa\n")
    f.write("Phone: 9876543210\n")
    f.write("Email: vishwa@gmail.com\n")

# Read the text file
with open("data.txt", "r") as f:
    text = f.read()

# Extract information using regular expressions
name = re.search(r"Name: (.*)", text)
phone = re.search(r"Phone: (\d+)", text)
email = re.search(r"Email: (\S+)", text)

print("Name:", name.group(1))
print("Phone:", phone.group(1))
print("Email:", email.group(1))
