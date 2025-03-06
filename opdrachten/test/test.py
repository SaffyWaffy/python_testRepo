def altijd_nul(a):
    if a > 0:
        return altijd_nul(a-1)
    return a


print(altijd_nul(input()))
