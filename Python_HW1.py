# 1.1. Ի՞նչ կպատասխանի ինտերպրետատորը ներքևում գրված արտահայտություններից յուրաքանչյուրին

# >>> 10
# answer: 10
# >>> 5 + 3 + 12
# answer: 20
# >>> 9 - 2
# answer: 7
# >>> 20 / 2
# answer: 10.0
# >>> (4 * 2) - (2 * 3)
# answer: 2
# >>> a = 3
# answer: nothing
# >>> b = a + 1
# answer: nothing
# >>> a + b + (a * b)
# answer: 19

# 1.3 Ստեղծեք ֆունկցիա, որը որպես արգումենտ ստանում է երեք թվեր
# # և վերադարձնում է դրանցից երկու մեծագույնների քառակուսիների գումարը։
def square_sum(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return b ** 2 + c ** 2


# 1.4 Նկարագրեք հետևյալ ֆունկցիայի աշխատանքը
def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b
# Ինչո՞վ է այն տարբերվում հետևյալ սահմանումից
def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    return a - b

# answer։ արդյունքով իրարից չեն տարբերվում՝ եթե if-ի պայմանը սխալ եղավ, ապա անցում է հաջորդ տողին,
# արդյունքում նույն բանն են երկուս էլ վերադարձնելու։ Else-ով տարբերակը ավելի պարզ է կարդացվում։

# 1.5.Ստեղծել ֆունկցիա, որը ստանում է երկու թվային արգումենտ` a և b,
# և վերադարձնում է a-ից մինչև b ընկած ամբողջ թվերի գումարը (a<b)։
def range_sum(a, b):
    rsum = 0
    for i in range(b + 1):
        rsum += i
    return rsum
# 1.6. Եթե a>b, ֆունկցիան պետք է վերադարձնի b-ից մինչև a ամբողջ թվերի գումարը։
def range_sum(a, b):
    if a > b:
        a,b = b,a
    rsum = 0
    for i in range(b + 1):
        rsum += i
    return rsum

# 1.7. Իրականացնել pow(a, b) ֆունկցիան՝ հաշվի առնելով, որ b-ն կարող է լինել նաև ոչ դրական
def pow(a, b):
    if a == 0 and b <0:
        raise ValueError('pow is nof defined for a==0 and n=b<0 arguments')
    if a < 0:
        a = 1/a
        b = -b
    res = 1
    count = 0
    if b == 0:
        return res
    while count < b:
        res = res * a
        count = count + 1
    return res

# 1.8. թվի խորանարդ արմատը
def cubic_root(target):
    root = 1
    while not check_ok(root, target):
        root = improve(root, target)
    return root

def check_ok(root, target):
    accuracy = 0.0001
    if abs(root ** 3 - target) < accuracy:
        return True
    else:
        return False

def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) / 3

# 1.9 # բացատրել, պարզել՝ որն է ռեկուրսիվ, որը պոչավոր ռեկուրսիվ
def inc(a):
	return a + 1
def dec(a):
	return a - 1

def add1(a, b):
	if a == 0:
		return b
	else:
		return inc(add1(dec(a), b))
# add1-ը ռեկուրսիվ ֆունկցիա է, օրինակ, a=2,b=3 -> inc(inc(add1(0,3))), նախորդ քայլերը պետք է պահվեն հիշողության մեջ։
# add2-ը նախորդ քայլերը կարող է չպահել, բավարար է վերջին քայլի արժեքը, ռեկուրսիան պոչավոր է։
def add2(a, b):
    if a == 0:
        return b
	else:
		return add2(dec(a), inc(b))


# 1.10 Ակերմանի ֆունկցիա
def ackermann(x, y):
	if y == 0:
		return 0
	elif x == 0:
		return 2 * y
	elif y == 1:
		return 2
	else:
		return ackermann(x - 1, ackermann(x, y - 1))

# ackermann(1, 5)-> 32
# ackermann(2, 4) = ackermann(3, 3) -> 65536

# a1: ackermann(0,n) -> one of base cases: 2*n

# a2: ackermann(1,n) -> n խորություն ունեցող ռեկուրսիա, օրինակ, n = 5-ի դեպքում կստացվի։
# ackermann(0,ackermann(0,ackermann(0,ackermann(0,ackermann(1,n-4))))) -> 2^5=32

# a3: ackermann(2,n) -> n-ից մեծ թվով խորության ռեկուրսիա, օրինակ, n = 3-i դեպքում կստացվի։
# ackermann(1,ackermann(1,ackermann(2,n-2))) -> 4*4 = 16
