key = "GAKQLA"

index = 0

string = """IOXWCAZUVQEIUNC EY HGVSDR MGDO YE SU FKH. HE GRO QYOTYWEFS. CE KHP RKSZEYSOBVU QOX TRU MRKAU YY AZ BKDV. WK DY DZT VROVPR ROCU PNJS. WHD EBA SI CEYPYDDIHLO VZR ZHO CTSNAZ QE TNE LQYK. CE RQGE GCAKTRKD KBW OL TRU MATK'C RLCQUZ TLTG. A LQYK CE LUWIKVO JZ BK CYHCUVT, KYOITG SD XOTEI BLUTDOHTNM.

NYM RO ZO DXP AADSJZROUW, QYD MIFU EHKM DXP KKY "CYVE ZHKJ EHK WBEYG IONU"

HE YHKBW MKED QRAON CEZN. GNYDJMUUC."""

encrypted = ""

for elem in string:
    if elem not in [" ", ".", ",", "'", "\"", "\n", "\r"]:
        encrypted += chr((((ord(elem) - 65) - (ord(key[index]) - 65)) % 26) + 65)
        index += 1

        if index == len(key):
            index = 0
    else:
        encrypted += elem

print(encrypted)
