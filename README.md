# xinqqi
-----
## Лабораторная работа 1
-----
-----
### Задание 1
``` python
name = input("Имя: ")
age = int(input("Возраст: "))
age = age+1
print("Привет, " + name+"! Через год тебе будет "+str(age)+".")
```
<img width="452" height="113" alt="image" src="https://github.com/user-attachments/assets/4e8fd0e8-9a8b-4166-9e27-6b404b1aa42e" />

### Задание 2
``` python
a=input("a: ")
b=input("b: ")
a=a.replace(",",".")
b=b.replace(",",".")
a=float(a)
b=float(b)
sum=a+b
avg=(a+b)/2.0
print("sum: %.2f; avg: %.2f" %(sum, avg))
```
<img width="423" height="100" alt="image" src="https://github.com/user-attachments/assets/9973d934-f1dc-4a79-8097-eba6a934796a" />

### Задание 3
``` python
price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print("База после скидки: %.2f" %(base))
print("НДС:               %.2f" %(vat_amount))
print("Итого к оплате:    %.2f" %(total))
```
<img width="382" height="174" alt="image" src="https://github.com/user-attachments/assets/894f905d-193a-497a-99dc-e60aad19a840" />


### Задание 4
``` python
m=int(input("Минуты: "))
h=m//60
m=m%60
print(f"{h:d}:{m:02d}")
```
<img width="363" height="76" alt="image" src="https://github.com/user-attachments/assets/3e03e864-287f-4266-bedf-53d924f19671" />

### Задание 5
``` python
fio = input("ФИО: ")
words = fio.split()

initials = ""
for w in words:
    i = "".join(w[0]).upper()
    initials = initials+i

fio = " ".join(words)
print("Инициалы: "+initials+".")
print("Длина (символов): ", len(fio))
```
<img width="464" height="215" alt="image" src="https://github.com/user-attachments/assets/aed0a3b1-ca1e-4ae9-ba15-66d8fca67b79" />

### Задание 6
``` python
N = int(input())

y = 0
n = 0
i = 1

for i in range(N):
    line = input().split()
    if line[-1].upper() == "TRUE":
        y += 1
    else:
        n += 1

print(y, n)
```
<img width="414" height="193" alt="image" src="https://github.com/user-attachments/assets/f843c515-4589-4962-a9e9-ec4553123e11" />
