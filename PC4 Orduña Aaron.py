#PROBLEMA 2
import re
regex = r'^[456]\d{15}$|^[456]\d{3}-\d{4}-\d{4}-\d{4}$'
evaluar = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456']

for t in evaluar:
    x = re.findall(regex, t )
    
    if x:
        print(f'{t} -> Valid')
    else:
        print(f'{t} -> Invalid')
        



# PROBLEMAS DIVERSOS
## FICHEROS

# Ejericio 1
import os

n = int(input("Ingrese un numero del 1 al 12: "))

file_name = "./tabla-{}.txt".format(n)

with open (file_name, mode = "w") as f:
    for i in range(1, 13):
        cadena = "{} x {} = {}\n".format(n,i, i*n)  
        f.write(cadena)


# Ejericio 2
n = int(input("Ingrese un numero del 1 al 12: "))

file_name = "./tabla-{}.txt".format(n)

try: 
    f = open(file_name, "r")
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

# Ejericio 3
n = int(input("Ingrese un numero del 1 al 12: "))
m = int(input("Ingrese un segundo numero del 1 al 12: "))

file_name = "./tabla-{}.txt".format(n)

with open (file_name, mode = "w") as f:
    for i in range(1, 13):
        cadena = "{} x {} = {}\n".format(n,i, i*n)  
        f.write(cadena)
try: 
    f = open(file_name, "r")
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    lines = f.readlines()
    print(lines[m - 1])


import re
## EXPRESIONES REGULARES
# Ejericio 1
# Cadena entrada
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
s
print(re.findall(r"@robot\d\W",s))

# Ejericio 2
# Cadena entrada
c = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
c
print(re.findall(r"User_mentions:\d",c))
print(re.findall(r"likes: \d",c))
print(re.findall(r"number of retweets: \d",c))

# Ejericio 3
from modulo import datos
path = './src/re/short_tweets.csv'
# Cadena entrada
analisis_sentimientos = datos.read_pandas(path,780,782)
for tweet in analisis_sentimientos:
    print(tweet)


# Ejericio 4   
regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    if re.match(regex, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   