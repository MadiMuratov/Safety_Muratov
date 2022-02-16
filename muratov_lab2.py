a=2
b=5
alf="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
shifr=""
deshifr=""
x=a
stroka=input('Введите строку ')
while x%33!=1:
  x=x+a
x=x/a
for i in range(len(stroka)):
  s=stroka[i]
  Sh=(a*alf.index(s)+b)%33
  shifr=shifr+alf[Sh]
print(shifr)
for i in range(len(stroka)):
  s=shifr[i]
  Sh=int((x*(alf.index(s)-b))%33)
  deshifr=deshifr+alf[Sh]
print(deshifr)


