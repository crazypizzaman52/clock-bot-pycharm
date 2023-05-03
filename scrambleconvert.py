# I put this all in another file because I never want to see this code again.

# this converts wca notation to the notation that optclock uses as its input, which is just a list of 14 numbers
def scrambler(s):
    n = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    try:
        before = s.split("y2")[0].split(" ")
        after = s.split("y2")[1].split(" ")
    except:
        before = s.split(" ")
        after = ""

    for i in before:
        if len(i) == 2:
            pass
        elif "ULDR" in i:
            x = i.split("ULDR")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "URDL" in i:
            x = i.split("URDL")[1]
            if x[1] == "+":
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
            if x[1] == "-":
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])

        elif "UL" in i:
            x = i.split("UL")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])

        elif "UR" in i:
            x = i.split("UR")[1]
            if x[1] == "+":
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
            if x[1] == "-":
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])

        elif "DL" in i:
            x = i.split("DL")[1]
            if x[1] == "+":
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
            if x[1] == "-":
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])

        elif "DR" in i:
            x = i.split("DR")[1]
            if x[1] == "+":
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "ALL" in i:
            x = i.split("ALL")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "ul" in i:
            x = i.split("ul")[1]
            if x[1] == "+":
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "ur" in i:
            x = i.split("ur")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "dl" in i:
            x = i.split("dl")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "dr" in i:
            x = i.split("dr")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])

        elif "U" in i:
            x = i.split("U")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])

        elif "R" in i:
            x = i.split("R")[1]
            if x[1] == "+":
                n[1] += int(x[0])
                n[2] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[1] -= int(x[0])
                n[2] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "D" in i:
            x = i.split("D")[1]
            if x[1] == "+":
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[5] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
                n[8] += int(x[0])
            if x[1] == "-":
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[5] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])
                n[8] -= int(x[0])

        elif "L" in i:
            x = i.split("L")[1]
            if x[1] == "+":
                n[0] += int(x[0])
                n[1] += int(x[0])
                n[3] += int(x[0])
                n[4] += int(x[0])
                n[6] += int(x[0])
                n[7] += int(x[0])
            if x[1] == "-":
                n[0] -= int(x[0])
                n[1] -= int(x[0])
                n[3] -= int(x[0])
                n[4] -= int(x[0])
                n[6] -= int(x[0])
                n[7] -= int(x[0])

    for i in after:
        if len(i) == 2:
            pass

        elif "ULDR" in i:
            x = i.split("ULDR")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[2] -= int(x[0])
                n[6] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[2] += int(x[0])
                n[6] += int(x[0])

        elif "URDL" in i:
            x = i.split("URDL")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[8] += int(x[0])

        elif "UL" in i:
            x = i.split("UL")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[2] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[2] += int(x[0])

        elif "UR" in i:
            x = i.split("UR")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[0] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[0] += int(x[0])

        elif "DL" in i:
            x = i.split("DL")[1]
            if x[1] == "+":
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[13] += int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[13] -= int(x[0])
                n[8] += int(x[0])

        elif "DR" in i:
            x = i.split("DR")[1]
            if x[1] == "+":
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[6] -= int(x[0])
            if x[1] == "-":
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[6] += int(x[0])

        elif "ALL" in i:
            x = i.split("ALL")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[2] -= int(x[0])
                n[6] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[2] += int(x[0])
                n[6] += int(x[0])
                n[8] += int(x[0])

        elif "ul" in i:
            x = i.split("ul")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[6] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[6] += int(x[0])
                n[8] += int(x[0])

        elif "ur" in i:
            x = i.split("ur")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[2] -= int(x[0])
                n[6] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[2] += int(x[0])
                n[6] += int(x[0])
                n[8] += int(x[0])

        elif "dl" in i:
            x = i.split("dl")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[2] -= int(x[0])
                n[6] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[2] += int(x[0])
                n[6] += int(x[0])

        elif "dr" in i:
            x = i.split("dr")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[2] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[2] += int(x[0])
                n[8] += int(x[0])

        elif "U" in i:
            x = i.split("U")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[0] -= int(x[0])
                n[2] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[0] += int(x[0])
                n[2] += int(x[0])

        elif "R" in i:
            x = i.split("R")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[0] -= int(x[0])
                n[6] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[0] += int(x[0])
                n[6] += int(x[0])

        elif "D" in i:
            x = i.split("D")[1]
            if x[1] == "+":
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[12] += int(x[0])
                n[13] += int(x[0])
                n[6] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[12] -= int(x[0])
                n[13] -= int(x[0])
                n[6] += int(x[0])
                n[8] += int(x[0])

        elif "L" in i:
            x = i.split("L")[1]
            if x[1] == "+":
                n[9] += int(x[0])
                n[10] += int(x[0])
                n[11] += int(x[0])
                n[13] += int(x[0])
                n[2] -= int(x[0])
                n[8] -= int(x[0])
            if x[1] == "-":
                n[9] -= int(x[0])
                n[10] -= int(x[0])
                n[11] -= int(x[0])
                n[13] -= int(x[0])
                n[2] += int(x[0])
                n[8] += int(x[0])

    r = ""
    for i in range(len(n)):
        n[i] = n[i] % 12
        if n[i] == 0:
            n[i] = 12
        r += str(n[i]) + " "
    return (r)


# this converts the notation optclock outputs to wca notation
def solve(s, m):
    print(s)
    s = s.split(" ")
    r = ""
    for i in range(len(s)):
        if "d" in s[i]:
            r += pincheck(s[i - 1], 'd')
            if s[i].split("d")[1] == "'":
                r += '1+ '
            elif s[i].split("d")[1] == '':
                r += '1- '
            else:
                if "6" in s[i].split("d")[1]:
                    r += "6+ "
                elif "'" in s[i].split("d")[1]:
                    r += s[i].split("d")[1].replace("'", "+") + " "
                else:
                    r += s[i].split("d")[1] + "- "
    if "y2" in m:
        r += "y2 "
    for i in range(len(s)):
        if "u" in s[i]:
            r += pincheck(s[i - 1], 'u')
            if s[i].split("u")[1] == "'":
                r += '1- '
            elif s[i].split("u")[1] == '':
                r += '1+ '
            else:
                if "6" in s[i].split("u")[1]:
                    r += "6+ "
                elif "'" in s[i].split("u")[1]:
                    r += s[i].split("u")[1].replace("'", "-") + " "
                else:
                    r += s[i].split("u")[1] + "+ "
    print(r)
    return r


# this converts the pin notation
def pincheck(p, side):
    if side == "u":
        if p == "UDDD":
            return ("UL")
        if p == "DUDD":
            return ("UR")
        if p == "DDUD":
            return ("DL")
        if p == "DDDU":
            return ("DR")
        if p == "UUDD":
            return ("U")
        if p == "DUDU":
            return ("R")
        if p == "DDUU":
            return ("D")
        if p == "UDUD":
            return ("L")
        if p == "UDDU":
            return ("ULDR")
        if p == "DUUD":
            return ("URDL")
        if p == "DUUU":
            return ("ul")
        if p == "UDUU":
            return ("ur")
        if p == "UUDU":
            return ("dl")
        if p == "UUUD":
            return ("dr")
        if p == "UUUU":
            return ("ALL")
    if side == "d":
        if p == "UDUU":
            return ("UL")
        if p == "DUUU":
            return ("UR")
        if p == "UUUD":
            return ("DL")
        if p == "UUDU":
            return ("DR")
        if p == "DDUU":
            return ("U")
        if p == "DUDU":
            return ("R")
        if p == "UUDD":
            return ("D")
        if p == "UDUD":
            return ("L")
        if p == "UDDU":
            return ("ULDR")
        if p == "DUUD":
            return ("URDL")
        if p == "DUDD":
            return ("ul")
        if p == "UDDD":
            return ("ur")
        if p == "DDDU":
            return ("dl")
        if p == "DDUD":
            return ("dr")
        if p == "DDDD":
            return ("ALL")
