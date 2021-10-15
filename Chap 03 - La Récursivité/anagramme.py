def listeAnagramme(mot):
    
    if mot=='':
        return ['']
    if len(mot)==1:
        return [mot]
        
    else:
        liste=[]
        for anagr in listeAnagramme(mot[1:]):
            for i in range(len(mot)):
                liste.append(anagr[:i] + mot[0:1] + anagr[i:])
        return liste

print(listeAnagramme("abcd"))
