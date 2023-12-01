import PrgCls
#Programme

try:
    lon = input("Longueur du rectangle en cm ?")
    lar = input("Largeur du rectangle en cm ?")

    rec = PrgCls.Rectangle(int(lon) , int(lar))

    print(f"le perimetre est : {rec.Perimetre()} cm")
    print(f"L'air est : {rec.Air()} cm")

    if rec.EstCarre():
        print("Ce n'est pas un rectangle")
    else:
        print("c'est un rectangle")

except:
    print("une erreur s'est produite")
