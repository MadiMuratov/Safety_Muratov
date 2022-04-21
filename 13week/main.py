file = open("input.txt", "r", encoding="utf-8")
file2 = open("output.txt", "a", encoding="utf-8")
str=file.read()


def f_key() :
    key = "314"
    for i in range(0, len(str)):
        key = key+key[i]
    return key

def crypt(stroka, key):
    shifr=""
    for i in range(0, len(stroka)):
        num = ord(stroka[i]) + int(key[i])
        shifr=shifr+chr(num)
    file2.write("\n"+"Ключ = "+key+"\n")
    file2.write("Шифр = "+shifr)
    print("Зашифровано")

def decrypt(stroka, key):
    deshifr=""
    for i in range(0, len(stroka)):
        num = ord(stroka[i]) - int(key[i])
        deshifr=deshifr+chr(num)
    file2.write("\n"+"Ключ = "+key+"\n")
    file2.write("Дешифр = "+deshifr)
    print("Расшифровано")

cryptOrNot=input("Вставьте текст в файл input.txt и введите команду\n crypt для шифровки\n decrypt для расшифровки\n")
if cryptOrNot=="crypt":
    crypt(str, f_key())
elif cryptOrNot=="decrypt":
    decrypt(str, f_key())
else : print("Неверная команда")