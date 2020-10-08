def in_ASCII(string): #функия представления символов в числовой код таблицы ASCII
    a = []
    for i in string:
        a.append(ord(i))
    return a


def encryption(list, step): #функция дообавление шага к нужным символам
    new_list = []
    for i in list:
        if i in AZ:
            i += step
            if i > 90: #проверка
                i = (i % 90) + 65
        elif i in az:
            i += step
            if i > 122: #проверка
                i = (i % 122) + 97
        elif i in AZ_Rus:
            i += step
            if i > 1071: #проверка
                i = (i % 1071) + 1040
        elif i in az_Rus:
            i += step
            if i > 1103: #проверка
                i = (i % 1103) + 1072
        new_list.append(i)
    return new_list


def decryption(new_list): #функция перевода числовых значений таблицы ASCII в символы
    a = str()
    for i in new_list:
        a += chr(i)
    return a


AZ = set(i for i in range(65, 91))
az = set(i for i in range(97, 123))
AZ_Rus = set(i for i in range(1040, 1072))
az_Rus = set(i for i in range(1072, 1104))

decr = open('source.txt', 'r')
encr = open('encryption.txt', 'w')
step = int(input())
for line in decr:
    encr.write(decryption(encryption(in_ASCII(line), step)))
    # print(decryption(encryption(in_ASCII(s), step)))
decr.close()
encr.close()
