import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8)) 

def cabecalho2(
        texto, # type: str
        alinhamento=True # type bool
        ): # type: (...) -> str
    if alinhamento == True:
        return 'a'
    elif alinhamento == False:
        return 'b'
    
print(cabecalho2(texto=42, alinhamento=True))