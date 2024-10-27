from Crypto.Util.number import long_to_bytes
from sympy import solve
from sympy.abc import x, y, z

#FLAG = open("flag.txt", "rb").read()
v1 = 4196604293528562019178729176959696479940189487937638820300425092623669070870963842968690664766177268414970591786532318240478088400508536
v2 = 11553755018372917030893247277947844502733193007054515695939193023629350385471097895533448484666684220755712537476486600303519342608532236
v3 = 14943875659428467087081841480998474044007665197104764079769879270204055794811591927815227928936527971132575961879124968229204795457570030
v4 = 6336816260107995932250378492551290960420748628

resultat = solve([x**3 + z**2 + y - v1, y**3 + x**2 + z - v2, z**3 + y**2 + x - v3, x + y + z - v4], [x,y,z], dict=True)
#print(resultat)
res = ""
for r in resultat:
    for l in r:
        res += long_to_bytes(r[l]).decode()
    res += "\n"

print(res)

#step = len(FLAG) // 3
#candies = [bytes_to_long(FLAG[i:i+step]) for i in range(0, len(FLAG), step)]

#cnd1, cnd2, cnd3 = candies

#with open('output.txt', 'w') as f:
#    f.write(f'v1 = {cnd1**3 + cnd3**2 + cnd2}\n')
#    f.write(f'v2 = {cnd2**3 + cnd1**2 + cnd3}\n')
#    f.write(f'v3 = {cnd3**3 + cnd2**2 + cnd1}\n')
#    f.write(f'v4 = {cnd1 + cnd2 + cnd3}\n')