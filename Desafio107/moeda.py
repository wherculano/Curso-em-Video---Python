def metade(valor):
    resp = float(valor / 2)
    return resp


def dobro(valor):
    resp = float(valor * 2)
    return resp


def aumentar(valor, taxa=0):
    resp = float(valor + (taxa / 100 * valor))
    return resp


def diminuir(valor, taxa=0):
    resp = float(valor - (taxa / 100 * valor))
    return resp
