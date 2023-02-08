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


