def kilogramos_gramos(kilos):
    formula = kilos * 1000
    return f"El resultado es {formula}"

def toneladas_gramos(t):
    formula = t * 1000000

    return f"El resultado es {formula}"


if __name__ == '__main__':
    kilos = 20
    t = 20
    print(kilogramos_gramos(kilos))
    print(toneladas_gramos(t))