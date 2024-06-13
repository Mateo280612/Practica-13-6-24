
x = {'data': 'Lunes','next': None}
y = {'data': 'Martes','next': None}

x['next'] = y

def presentacion():
    nodo_inicial = x
    while nodo_inicial:
        print(nodo_inicial['data'], end = '->' if nodo_inicial['next'] is not None else '\n')
        nodo_inicial = nodo_inicial ['next']

presentacion()
