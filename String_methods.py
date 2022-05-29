#Իրականացնել string-ի տաս մեթոդները որպես ֆունկցիաներ

# 0. find
def myfind(text, part):
    j = len(part)
    for i in range(len(text)):
        if text[i:i+j] == part:
                return i
    return -1

# 1. capitalize
def mycapitalize(text):
    new_text = text
    letters = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h",
               "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q",
               "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}

    def find_key(s):
        for key, letter in letters.items():
            if s == letter:
                return key

    if text[0] not in letters:
        new_text = find_key(text[0]) + text[1:]
    for i in range(1,len(text)):
        if text[i] in letters:
            new_text = new_text[0] + new_text[1:i] + letters[text[i]] + new_text[i+1:]
    return new_text


# 2. replace
def myreplace(text, part, newpart):
    new_text = ""
    ind1 = len(part)
    while text.find(part) >=0:
        ind0 = text.find(part)
        if ind0 == 0:
            new_text = newpart + text[ind1:]
        new_text = text[:ind0] + newpart + text[ind0+ind1:]
        text = new_text
    return new_text

# 3. count
def mycount(text, part):
    count = 0
    ind1 = len(part)
    while text.find(part) >= 0:
        ind0 = text.find(part)
        text = text[ind0+ind1:]
        count += 1
    return count

# 4. endswith
def myend(text, part):
    text = text[::-1]
    part = part[::-1]
    ind1 = len(part)
    if text[:ind1] == part:
        return True
    return False

# 5.startswith
def mystart(text, part):
    ind1 = len(part)
    if text[:ind1] == part:
        return True
    return False

# 6. rfind
def myrfind(text, part):
    j = len(part)
    count = 0
    for i in range(len(text)):
        if text[i:i+j] == part:
            count +=1
            if mycount(text,part) == count:
                return i
    return -1


# 7. join
def myjoin(text, part):
    new_text = ""
    for i in range(len(text)-1):
        new_text += text[i]
        new_text+= part
    return new_text + text[-1]

# 8. strip
def mystrip(text):
    new_text = ""
    for i in text:
        if i != " ":
            new_text += i
    return new_text

# 9. lower --> same logic as in capitalize
