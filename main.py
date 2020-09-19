def in_ASCII(string):
    a = []
    for i in string:
        a.append(ord(i))
    return a


def encryption(list, step):
    new_list = []
    for i in list:
        if i in AZ:
            i += step
            if i > 90:
                i = abs(90 - i) + 65
        elif i in az:
            i += step
            if i > 122:
                i = abs(122 - i) + 97
        elif i in AZ_Rus:
            i += step
            if i > 1071:
                i = abs(1071 - i) + 1040
        elif i in az_Rus:
            i += step
            if i > 1103:
                i = abs(1103 - i) + 1072
        new_list.append(i)
    return new_list


def decryption(new_list):
    a = str()
    for i in new_list:
        a += chr(i)
    return a


AZ = set(i for i in range(65, 91))
az = set(i for i in range(97, 123))
AZ_Rus = set(i for i in range(1040, 1072))
az_Rus = set(i for i in range(1072, 1104))

s = input()
step = int(input())
print(decryption(encryption(in_ASCII(s), step)))