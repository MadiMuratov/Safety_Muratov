stroka=input()
shifr=[]
deshifr=[]
key="314"
for i in range(0,len(stroka)-3):
  key=key+key[i]
print(key)
for i in range(0,len(stroka)):
  per=ord(stroka[i])+int(key[i])
  shifr.append(chr(per))
print("".join(shifr))
for i in range(0,len(stroka)):
  per=ord(shifr[i])-int(key[i])
  deshifr.append(chr(per))
print("".join(deshifr))

