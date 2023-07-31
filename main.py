import testodin
import predkosx
import math
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
print(predkosx.pt(2,4))