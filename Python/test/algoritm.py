import math
import turtle
def ruutborrand(a, b, c):
    if a == 0:
        if c == 0:
            if b == 0:
                return 0
            else:
                return "x = 0"
        else:
            if b == 0:
                return False
            else:
                return f"x = {float(c/b)}"
    else:
        if b*b-4*a*c < 0:
            return f"Lahendid puuduvad"
        else:
            return f"x1 = {(-b+math.sqrt(b*b-4*a*c))/2*a} x2 = {(-b-math.sqrt(b*b-4*a*c))/2*a}"
        
        
        
        
        
def Tsykkel():
    sisend = int(input("Kui kaugel on maa kuust?: "))
    kuu_kaugus=10000000
    while True:
        if kuu_kaugus == sisend:
            break
        else:
            if kuu_kaugus > sisend:
                print("Rohkem")
                sisend = int(input("proovi uuesti.: "))
            else:
                print("Vahem")
                sisend = int(input("Proovi uuesti.: "))
                
kiirus = 5000
        
def pikkuse_kontsant():
    return kiirus
        
def bassein(kiirus):

    pikkus = int(23434.5334)  