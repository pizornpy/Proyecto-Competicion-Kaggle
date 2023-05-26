def limpiar_os(col):
    return col.apply(lambda x: 1 if x == "Windows" else 0) #función muy sencilla para limpiar el OS


def limpiar_sc(col):
    for v in col: 
        res = []
        for l in v:
            if l.isdigit(): 
                res.append(l):

            else: 
                pass 
    
        g1 = res[:3]
        g2 = res[4:]
    
    return col.apply(lambda x:g1*g2)



