from datetime import date,datetime

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

def sissenumb(i:list,p:list):
    nimi=input("Kelle palk tahad leia? ")
    while nimi not in i:
        nimi=input("kirjuta õige nimi ")
    n=i.count(nimi)
    if n!=1:
        print(f"Siin on mõned inimesed kes nimi on {nimi}") 
        kopia=i.copy()
        for i in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{i+1} {nimi} saab {p[ind]}")
    else:
        ind=i.index(nimi)
        print(f"{nimi} saab {p[ind]}")
       

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

def top3(i:list,p:list): 
    kopia=p.copy()
    for i in range(3):
        ind=kopia.index(min(kopia))
        print(f"{i+1} inimene - {i[ind]} saab väikse palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)
    kopia=p.copy()
    for i in range(3):
        ind=kopia.index(max(kopia))
        print(f"{i+1} inimene - {i[ind]} saab suur palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(p)+1)

def keskmine(i:list,p:list):
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for i in range(len(i)):
        if p[i]>=kesk:
            print(f"{i[i]} saab suurem kui keskmine palk, ta saab {p[i]}")
