def limpiar_os(col):
    return col.apply(lambda x: 1 if x == "Windows" else 0) #función muy sencilla para limpiar el OS

def limpiar_sc(col):
    res = []
    for v in col:
        cleaned_values = []
        for l in v:
            if l.isdigit():
                cleaned_values.append(l)
        res.append(cleaned_values)

    g1 = [''.join(x[:3]) for x in res]  # Sacamos los primeros 4 dígitos y los unimos para multiplicar
    g2 = [''.join(x[4:]) for x in res]  #Pillamos el resto y hacemos otro grupo

    result = [int(x) * int(y) for x, y in zip(g1, g2)]  # Multiplicacmos los elementos tras convertirlos a int

    return result

