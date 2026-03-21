p = 2
coef = [9, -5, 0, 2, 9, 4, 2, 4, 7, 8, 1,6]

def horn(coef, p):
    res = p*coef[0]+coef[1]
    for i in range(len(coef)-2):
        # print(i+2,coef[i+2])
        res=p*res+coef[i+2]
    # print(res)
    return res

def horn_mal(coef, p):
    res = 0
    for i in range(len(coef)):
        res = res + coef[i]*p**(len(coef)-1-i)
    return res


print(horn(coef,p))
print(horn_mal(coef,p))