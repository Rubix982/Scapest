string = "Among you is one of us. Find one of us, find all of us. The key to the next puzzle is IULHQGVKLS - look at the index of the numbers. "

encrypted = ""

# for i in range(0, len(string)):
for index, elem in enumerate(string):
    if elem not in [" ", ".", ",", "'", "-"]:
        if 65 <= ord(elem) <= 92:
            encrypted += chr(((((ord(elem) - 65) + ((index + 1) * 2) % 26)) % 26) + 65)
        elif 97 <= ord(elem) <= 122:
            encrypted += chr(((((ord(elem) - 97) + ((index + 1) * 2) % 26)) % 26) + 97)
    else:
        encrypted += elem

print(encrypted)
