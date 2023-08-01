import dane
import ob
import testodin
import predkosx
import Cacl.ob
from Cacl.dane import dane

#import  math
#print("hello PYthon Początek")
##bawie sie debuggerem
#num=6
##num+=1
#num+=1
#num+=1
#num+=1
#num=math.pow(num,2)
#if num>2:
##    print("DONKI KONG")
#print(num)
#num+=1
testodin.sayhello()
droga=int(input("jaką droge przebyłęs? (w km )"))
czas=int(input("jak długo zajeło ci to ? ( w h)"))
sr=predkosx.sp(czas,droga)
print(f"Było by to {sr} km na h  ")
print(predkosx.pt(3,4))

pk,op,ok=dane()
print(f"oto twoja lokata {Cacl.ob.lokata(pk,op,ok)}")