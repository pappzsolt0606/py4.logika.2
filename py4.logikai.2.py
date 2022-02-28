'''
2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi,
hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni!
Például így: Jön Henrik ma kosarazni? (igen/nem).
A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
'''
#x = Henrik
#y = Hanna
kerdesx = input('Jössz e kosarazni? ')
kerdesy = input('Jössz e kosarazni? ')
kerdesxy = input('Jöttök e kosarazni? ')

if kerdesx == "Jövök":
    print("Igen")
else:
    print("Nem")
    
if kerdesy == "Jövök":
    print("Igen")
else:
    print("Nem")
    
if kerdesxy == "Jövünk":
    print("Igen")
else:
    print("Nem")
    
'''
#ez egy nem befejezett próbálkozás
if kerdesx == "Jövök" and  != kerdesy:
    print("Csak az egyikőjük jön kosarazni")
if kerdesy == "Jövök" and  != kerdesx:
    print("Csak az egyikőjük jön kosarazni")
if kerdesxy != "Jövünk":
    print("Egyikőjük sem jön")
if kerdesxy == "Jövünk":
    print("Mindkettőjük jön")
'''

