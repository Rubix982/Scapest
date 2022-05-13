string = """Cquvq mem eq qrk yr kk. Diph wxq ex qq, jovn obd kd ww. Dts cyu tq zpo bupn nubdrm ug AOHFQIZQTC - diki cx brq yfxav qj brq dmgxcru.

Sz jzy berexbwqbj zkp epgacuqi, dgsvsxg, zylynytwvk, mfjk, wow cqvx vahz ap kvfqzehy uakxovq tej umu xu qgwtw umu st qqhjahc tji vojh hlkzlgq.

Fc yyp tji mxhsbgja apwcmb hxw dmlfix yr jzy cnxirwzq jzy laoi wp meml ergezmcf dwgaqiu.

Cqs qiq sqst.

Pukn uiulka,
KEMFZL'V EWE ZYCY RO OTWG, IZYNJOEO?"""

encrypted = ""

# for i in range(0, len(string)):
for index, elem in enumerate(string):
    if elem not in [" ", ".", ",", "'", "-", "\n", "\r", "?"]:
        if 65 <= ord(elem) <= 92:
            encrypted += chr(((((ord(elem) - 65) - ((index + 1) * 2) % 26)) % 26) + 65)
        elif 97 <= ord(elem) <= 122:
            encrypted += chr(((((ord(elem) - 97) - ((index + 1) * 2) % 26)) % 26) + 97)
    else:
        encrypted += elem

print(encrypted)
