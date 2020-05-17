import sys,os,random


a = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"020"+str(random.randint(0,9))
aa = "a"

b = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"040"+str(random.randint(0,9))
bb = "b"

c = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"060"+str(random.randint(0,9))
cc = "c"

ç = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"080"+str(random.randint(0,9))
çç = "ç"

d = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"100"+str(random.randint(0,9))
dd = "d"

e = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"120"+str(random.randint(0,9))
ee = "e"

f = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"140"+str(random.randint(0,9))
ff = "f"

g = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"160"+str(random.randint(0,9))
gg = "g"

ğ = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"180"+str(random.randint(0,9))
ğğ = "ğ"

h = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"200"+str(random.randint(0,9))
hh = "h"

ı = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"220"+str(random.randint(0,9))
ıı = "ı"

i = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"240"+str(random.randint(0,9))
ii = "i"

j = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"260"+str(random.randint(0,9))
jj = "j"

k = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"280"+str(random.randint(0,9))
kk = "k"

l = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"300"+str(random.randint(0,9))
ll = "l"

m = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"320"+str(random.randint(0,9))
mm = "m"

n = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"340"+str(random.randint(0,9))
nn = "n"

o =str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"360"+str(random.randint(0,9))
oo = "o"

ö = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"380"+str(random.randint(0,9))
öö = "ö"

p = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"400"+str(random.randint(0,9))
pp = "p"

r = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"420"+str(random.randint(0,9))
rr = "r"

s = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"440"+str(random.randint(0,9))
ss = "s"

ş = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"460"+str(random.randint(0,9))
şş = "ş"

t = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"480"+str(random.randint(0,9))
tt = "t"

u = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"500"+str(random.randint(0,9))
uu = "u"

ü = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"520"+str(random.randint(0,9))
üü = "ü"

v = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"540"+str(random.randint(0,9))
vv = "v"

y = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"560"+str(random.randint(0,9))
yy = "y"

z = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"580"+str(random.randint(0,9))
zz = "z"

metin = sys.argv[1]
sifre = []


for tx in metin:
    if tx == aa:
        sifre.append(a)
    if tx == bb:
        sifre.append(b)
    if tx == cc:
        sifre.append(c)
    if tx == çç:
        sifre.append(ç)
    if tx == dd:
        sifre.append(d)
    if tx == ee:
        sifre.append(e)
    if tx == ff:
        sifre.append(f)
    if tx == gg:
        sifre.append(g)
    if tx == ğğ:
        sifre.append(ğ)
    if tx == hh:
        sifre.append(h)
    if tx == ıı:
        sifre.append(ı)
    if tx == ii:
        sifre.append(i)
    if tx == jj:
        sifre.append(j)
    if tx == kk:
        sifre.append(k)
    if tx == ll:
        sifre.append(l)
    if tx == mm:
        sifre.append(m)
    if tx == nn:
        sifre.append(n)
    if tx == oo:
        sifre.append(o)
    if tx == öö:
        sifre.append(ö)
    if tx == pp:
        sifre.append(p)
    if tx == rr:
        sifre.append(r)
    if tx == ss:
        sifre.append(s)
    if tx == şş:
        sifre.append(ş)
    if tx == tt:
        sifre.append(t)
    if tx == uu:
        sifre.append(u)
    if tx == üü:
        sifre.append(ü)
    if tx == vv:
        sifre.append(v)
    if tx == yy:
        sifre.append(y)
    if tx == zz:
        sifre.append(z)
    else:
        pass



dosya = open("sifre.txt","w")
for sf in sifre:
    dosya.writelines(str(sf))

