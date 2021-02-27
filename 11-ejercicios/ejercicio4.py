"""
EJERCICIO 4
- Crear un script que tenga 4 variables; una lista, un string, un entero y un booleano
- Imprimmir mensaje con tipo de cada variable
"""
# def comprobarTipado(dato):
def traducirTipo(tipo):
    result = None

    if tipo == list:
        result = "LISTA"
    elif tipo == str:
       result = "STRING"
    elif tipo == int:
       result = "ENTERO"
    elif tipo == bool:
       result = "BOOLEANO"
    return result



def comprobarTipado(dato,tipo):
    test = isinstance(dato,tipo)
    result =" "
    if test:
        result = print(f"Este dato es del tipo {traducirTipo(tipo)}")
    else:
       result = print("El tipo de dato no es correcto")
    
    return result

mi_lista = ["Hola Mundo",77]
texto = "Hola Sol"
numero = 100
verdadero = True


comprobarTipado(mi_lista,int)
comprobarTipado(mi_lista,list)
comprobarTipado(texto,str)
comprobarTipado(numero,int)
comprobarTipado(verdadero,bool)
