import random
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters=upper_letters.lowercase()
digits='0123456789'
symbols="()[]{}.,:-_/\|?+*#"
upper,lower,numbers,symboicnumbers=True,True,True,True

all=""
if upper:
    all+=upper_letters
if lower:
    all+=lower_letters
if numbers:
    all+=digits
if symbolicnumbers:
    all+=symbols

length=40;
amount=20;

for i in range(amount):
    password=" ".join(random.sample(all,length))
    print(password)
    