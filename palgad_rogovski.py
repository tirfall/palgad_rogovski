from module1 import *
import pickle
import os

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A"]

filename="Palk"
filename2="Nimi"
if not os.path.exists(filename): 
    with open(filename, "wb") as f: 
        pickle.dump(palgad, f)
else: 
    with open(filename, "rb") as f:
        palgad = pickle.load(f)

if not os.path.exists(filename2): 
    with open(filename2, "wb") as f: 
        pickle.dump(inimesed, f)
else: 
    with open(filename2, "rb") as f:
            inimesed = pickle.load(f)

while True:
    try:
        
        choice=int(input("Menu:\n0 - exit\n1 - Lisa andmed\n2 - Vaata andmed\n3 - Kustuta andmed\n4 - maximum palk\n5 - minimum palk\n6 - sort palgad\n7 - Leia palk nimi abiga\n8 - Leia palk nimi abiga\n8 - Leia kes saab palk suurem, väiksem või täpselt kui palk\n9 - Leia top 3 inimesed kes saab väike palk ja suur palk\n10 - Otsi keskmine\n17 - Adminpanel\n"))
        if choice==0:
            break
        elif choice==1:
            inimesed,palgad=Lisa_andmed(inimesed,palgad)
            print(inimesed,"\n",palgad)
        elif choice==2:
            print(inimesed,"\n",palgad)
        elif choice==3:
            inimesed,palgad=kustutamine(inimesed,palgad)
            print(inimesed,"\n",palgad)
        elif choice==4:
            inimesed,palgad=maxpalk(inimesed,palgad)
        elif choice==5:
            inimesed,palgad=minpalk(inimesed,palgad)
        elif choice==6:
            inimesed,palgad=sortpalk(inimesed,palgad)
            print(inimesed,"\n",palgad)
        elif choice==7:
            inimesed,palgad=findnimi(inimesed,palgad)
        elif choice==8:
            inimesed,palgad=palko(inimesed,palgad)
        elif choice==9:
            tomami(inimesed,palgad)
        elif choice==10:
            keskmine(inimesed,palgad)
        elif choice==11:
            tulumaks(inimesed,palgad)
        elif choice==12:
            palgad,inimesed=sortpalk(palgad,inimesed)
            print(inimesed,"\n",palgad)
        elif choice==13:
            inimesed,palgad=lowav(inimesed,palgad)
        elif choice==14:
            inimesed,palgad=suurtitle(inimesed,palgad)
        elif choice==15:
            inimesed,palgad=fromnyear(inimesed,palgad)
        elif choice==16:
            inimesed,palgad=every3(inimesed,palgad)
        elif choice==17:
            passans=int(input("Enter password:"))
            if passans==8484:
                while True:
                    adminchoice = int(input("Menu:\n1 - load last version\n2 - Load reserv version\n3 - Save version\n4 - exit\n"))
                    if adminchoice == 1:
                        loading
                        print("Succesful")
                    elif adminchoice == 2:
                        print()
                    elif adminchoice == 3:
                        print()
                    elif adminchoice == 4:
                        break
                    else:
                        print("Vale number")
                        ValueError
            else:
                print("Vale pass")
    except ValueError:
        print("Vale number")

with open(filename, "wb") as f:
                pickle.dump(palgad, f)
with open(filename2, "wb") as f:
                pickle.dump(inimesed, f)

