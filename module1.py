from datetime import date,datetime
import pickle
import os

def Lisa_andmed(i:list,p:list):
    """Kirjeldus
    :param list i: Inimeste jarjend
    :param list p: Palgade jarjend
    :rtype: list,list
    """
    n=int(input("Mitu inimest:"))
    for j in range (n):
        nimi=input("Lisa nimi:")
        palk=int(input("Lisa palk:"))
        i.append(nimi)
        p.append(palk)
    return i,p

def kustutamine(i:list,p:list):
    """Kirjeldus
    :Kustuta list i: Inimeste jarjend
    :Kustuta list p: Palgade jarjend
    :rtype: list,list
    """
    nimi=input("sisesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range (n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)

    return i,p

def maxpalk(i:list,p:list):

    ans=max(p)
    ind=p.index(ans)
    nimi=str(i[ind])
    print(nimi,ans)
    return ans,nimi

def minpalk(i:list,p:list):

    ans=min(p)
    ind=p.index(ans)
    nimi=i[ind]
    print(nimi,ans)
    return ans,nimi

def sortpalk(i:list,p:list):
    v=int(input("1-kaheneb,2-kasveb"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    else:
        #palk=list(map(int,p))
        #palk.sort()
        #ind=list(p.index(palk))
        #nimi=list(i[ind])
        #print(palk)
        #print(nimi)
        print()
    return i,p

def findnimi(i:list,p:list):
    nimi=input("sisesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range (n):
            ind=i.index(nimi)
            print(i[ind])
            print(p[ind])

    return i,p

       

def palko(i:list,p:list):
    palk=input("Kirjuta igasugune palk ")
    while palk.replace(".","",1).isdigit()==False: 
        palk=input("Kirjuta õige palk ")
    palk=float(palk)
    for x in range(len(i)):
        if p[x]>palk: 
            print(f"{i[x]} saab suurem kui {palk}")
        elif p[x]<palk: 
            print(f"{i[x]} saab väiksem kui {palk}")
        else:
            print(f"{i[x]} saab täpselt {palk}")
    return i,p

def tomami(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    kopia=y.copy()
    for i in range(3):
        ind=kopia.index(min(kopia))
        print(f"{i+1} inimene - {x[ind]} saab väikse palk: {y[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(y)+1)
    kopia=y.copy()
    for i in range(3):
        ind=kopia.index(max(kopia))
        print(f"{i+1} inimene - {x[ind]} saab suur palk: {y[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(y)+1)

def keskmine(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    kesk=sum(y)/len(y)
    print(f"Keskmine palk on {kesk}")
    for i in range(len(x)):
        if y[i]>=kesk:
            print(f"{x[i]} saab suurem kui keskmine palk, ta saab {y[i]}")

def tulumaks(x:list,y:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    for i in range(0,len(y)):
        if y[i]<500:
            palk=y[i]
        elif 500>=y[i]<=1200:
            palk=(y[i]-500)-(y[i]-500)*0.2
        elif 1200>y[i]>=2099:
            palk=(500-(5/9)*(y[i]-1200))-(500-(5/9)*(y[i]-1200))*0.2
        else:
            palk=y[i]*0.2
        print(f"{x[i]} on maksuvaba palk {palk}")


def lowav(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    x1=[] 
    y1=[]
    kesk=sum(y)/len(y)
    print(f"Keskmine palk on {kesk}")
    for i in range(0,len(x)):
        if y[i]>kesk:
            y1.remove(y[i])
            x1.remove(x[i])
    x=x1 
    y=y1
    return x,y

def suurtitle(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    for i in range(0,len(x)):
        x[i]=x[i].title()
        y[i]=round(y[i],1) 
        y[i]=int(y[i])
    return x,y

def fromnyear(x:list,y:list):

    return x,y

def every3(x:list,y:list):

    return x,y

def loading(filename="Palk",filename2="Nimi"):
    with open(filename, "rb") as f:
        palgad = pickle.load(f)
    with open(filename2, "rb") as f:
            inimesed = pickle.load(f)
