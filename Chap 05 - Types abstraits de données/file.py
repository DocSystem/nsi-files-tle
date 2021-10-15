def fileCree():
    return []

def fileTaille(F):
    return len(F)

def fileEstVide(F):
    return fileTaille(F) == 0

def fileAjouterFin(F, e):
    F.append(e)

def fileRetirerTete(F):
    if fileEstVide(F):
        return None
    e = F[0]
    del F[0]
    return e

def fileTete(F):
    if fileEstVide(F):
        return None
    return F[0]