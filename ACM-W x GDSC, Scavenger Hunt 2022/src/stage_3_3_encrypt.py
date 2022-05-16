key = "GAKQLA"

index = 0

string = """CONGRATULATIONS ON HAVING MADE IT SO FAR. WE ARE ANONYMOUS. WE ARE RESPONSIBLE FOR THE BREAK IN AT BANK. WE DO NOT PREFER LOSE ENDS. MRS EVA IS RESPONSIBLE FOR THE MISHAP AT THE BANK. WE HAVE ACQUIRED ALL OF THE BANK'S BACKUP DATA. A BANK WE BELIEVE TO BE CORRUPT, AIDING IN MONEY LAUNDERING.

NOW GO TO THE AUDITORIUM, AND GIVE THEM THE KEY "SIKE THAT THE WRONG CODE"

HEH, BY THE WAY, A FLAG AWAITS YOU IN THE NEW BUILDING AS WELL.WAVE IT WHEN YOU FOUND IT, AND BRING IT TO US

WE SHALL MEET AGAIN SOON. ANONYMOUS."""

encrypted = ""

# for i in range(0, len(string)):
for elem in string:
    if elem not in [" ", ".", ",", "'", "\"", "\n", "\r"]:
        encrypted += chr((((ord(elem) - 65) + (ord(key[index]) - 65)) % 26) + 65)
        index += 1

        if index == len(key):
            index = 0
    else:
        encrypted += elem

print(encrypted)
