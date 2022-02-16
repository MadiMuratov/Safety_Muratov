a=7
b=3
m=4096
alf="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
shifr=""
deshifr=""
gamma=[2020]
stroka=input("Введите строку ")
for i in range(1,len(stroka)):
  y=(a*gamma[i-1]+b) % m
  gamma.append(y)
print(gamma)
for i in range(0,len(stroka)):
  shifr=shifr+alf[(gamma[i]+ alf.index(stroka[i]))%33]
print(shifr)
for i in range(0,len(stroka)):
  deshifr=deshifr+alf[(alf.index(shifr[i])+33-gamma[i])%33]
print(deshifr)
