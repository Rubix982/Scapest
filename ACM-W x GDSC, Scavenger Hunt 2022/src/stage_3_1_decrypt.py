key = "GAKQLA"

string = "Cquvq mem eq qrk yr kk. Diph wxq ex qq, jovn obd kd ww. Dts cyu tq zpo bupn nubdrm ug XLECNFWNQZ - diki cx brq dmgxcru un fvu inbet"

encrypted = ""

# for i in range(0, len(string)):
for index, elem in enumerate(string):
    if elem not in [" ", ".", ",", "'", "-"]:
        if 65 <= ord(elem) <= 92:
            encrypted += chr(((((ord(elem) - 65) - ((index + 1) * 2) % 26)) % 26) + 65)
        elif 97 <= ord(elem) <= 122:
            encrypted += chr(((((ord(elem) - 97) - ((index + 1) * 2) % 26)) % 26) + 97)
    else:
        encrypted += elem

print(encrypted)
