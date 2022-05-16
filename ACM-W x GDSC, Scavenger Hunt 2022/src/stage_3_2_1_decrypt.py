string = """KTD QNG PDIK BTB RB?"""

encrypted = ""

# for i in range(0, len(string)):
for index, elem in enumerate(string):
    if elem not in [" ", ".", ",", "'", "-", "\n", "\r", "?"]:
        if 65 <= ord(elem) <= 92:
            encrypted += chr(((((ord(elem) - 65) - ((index + 1) * 2 + 1) % 26)) % 26) + 65)
        elif 97 <= ord(elem) <= 122:
            encrypted += chr(((((ord(elem) - 97) - ((index + 1) * 2 + 1) % 26)) % 26) + 97)
    else:
        encrypted += elem

print(encrypted)
