from module1 import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A"]

while True:
    try:
        
        choice=int(input("Menu:\n0 - exit\n1 - Lisa andmed\n2 - Vaata andmed\n3 - Kustuta andmed\n4 - maximum palk\n5 - minimum palk\n6 - sort palgad\n7 - Otsi palk\n7 - Otsi palk\n"))
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
            inimesed,palgad=sissenumb(inimesed,palgad)
        elif choice==9:
            inimesed,palgad=palko(inimesed,palgad)
        elif choice==10:
            inimesed,palgad=top3(inimesed,palgad)
        elif choice==11:
            inimesed,palgad=keskmine(inimesed,palgad)
        elif choice==12:
            inimesed,palgad=findnimi(inimesed,palgad)
        elif choice==13:
            inimesed,palgad=findnimi(inimesed,palgad)
        elif choice==14:
            inimesed,palgad=findnimi(inimesed,palgad)
        elif choice==15:
            inimesed,palgad=findnimi(inimesed,palgad)
    except ValueError:
        print("Vale number")

