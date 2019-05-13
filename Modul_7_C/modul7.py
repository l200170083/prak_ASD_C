#No.1
import re

print ("Nomor 1")
f = open ('Indonesia.txt', 'r')
p = r'me[\w\.-]+'
string = re.findall(p, f.read())
print (string)

#No.2
import re

print ("Nomor 2")
f = open('Indonesia.txt', 'r')
p = r'di[\w\.-]+'
string = re.findall(p, f.read())
print (string)

#No.3
import re

print ('Nomor 3')
f = open ('Indonesia.txt', 'r')
r = r'di\s[\w\.-]+'
string3 = re.findall(r, f.read())
print (string3)

#No.4
import re

print ("Nomor 4")
f = open('KEI.html', 'r')
t = r'tittle="([\w\.-]+)">[\w\.-]+</a></td>\n<td>\d.\d\d</td>\n<td>\d.\d\d</td>\n<td>\d.\d\d</td>\n<td>(\d.\d\d)</td>'
string4 = re.findall(t, f.read())
print (string4)
