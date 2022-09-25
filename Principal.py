import os
from Clases import producto as p, ListaProd as lstP
listaProd = lstP()


def menu():
    print("1. Registrar producto")
    print("2. Modificar prodcuto")
    print("3. Buscar por código")
    print("4. Buscar por nombre")
    print("5. Buscar por precio")
    print("6. Mostrar productos con existencia menor que la mínima")
    print("7. Eliminar producto")
    print("8. Salir")
    op = int(input("Digite una opcion: "))
    return op


def agregarProducto():
    os.system('cls')
    print("Agregando Producto")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    descrip = input("Descripción: ")
    precio = input("Precio $: ")
    exist = input("Existencia: ")
    existMin = input("Existencia mínima: ")
    prodct = p(codigo, nombre, descrip, precio, exist, existMin)
    listaProd.agregar(prodct)
    print("="*50)


def modificarProducto():
    os.system('cls')
    print("Modificando Registro")
    codigo = input("Código: ")
    pd, posc = listaProd.buscarPorCodigo(codigo)
    print(f"""
    Nombre Actual: {pd.Nombre}
    Descripcion Actual: {pd.Descripcion}
    Precio Actual C$: {pd.Precio}
    Existencia Actual: {pd.Existencia}
    Existencia mínima: Actual {pd.ExistenciaMinima}
    """)
    print("="*50)
    print("Nuevos Datos")
    nNom = input("Nombre: ")
    nDesc = input("Descripción: ")
    nPrc = input("Precio C$: ")
    nExist = input("Existencia: ")
    nExistMin = input("Existencia mínima: ")
    print("="*50)
    nPrdct = p(pd.Codigo, nNom, nDesc, nPrc, nExist, nExistMin)
    listaProd.editar(nPrdct, posc)


def buscarCod():
    os.system('cls')
    print("="*50)
    print("Buscando por Código")
    codi = input("Código: ")
    p, posc = listaProd.buscarPorCodigo(codi)
    try:
        if p.Codigo != None:
            print(p)
            print("="*50)
        else:
            print("Operación cancelada")
            print("="*50)
    except Exception as ex:
        print("Continúa")
        print("="*50)


def buscarNom():
    os.system('cls')
    print("="*50)
    print("Buscando por Nombre")
    nomb = input("Nombre: ")
    try:
        p, posc = listaProd.buscarPorNombre(nomb)
        if p.Nombre != None:
            print(p)
            print("="*50)
    except Exception as ex:
        print("Continúa")
        print("="*50)


def buscarPr():
    os.system('cls')
    print("="*50)
    print("Buscando por Precio")
    preci = input("Precio: ")
    try:
        p, posc = listaProd.buscarPorPrecio(preci)
        if p.Precio != None:
            print(p)
            print("="*50)
    except Exception as ex:
        print("Continúa")
        print("="*50)


def mostrarMinExist():
    os.system('cls')
    print("="*50)
    print("Mostrando...")
    try:
        p, posc = listaProd.buscarExistenciaMin()
        print(p)
        print("Continúa")
    except Exception as ex:
        print("="*50)


def eliminar():
    os.system('cls')
    print("Eliminar")
    cod = input("Codigo: ")
    pd, posc = listaProd.buscarPorCodigo(cod)
    print(f"""¿De verdad desea eliminar este producto? {pd}""")
    resp = input("SI - NO: ")
    if resp.upper() == "SI":
        listaProd.eliminar(pd)
    else:
        print("Operación cancelada")
        print("="*50)

def main():
    op = 0
    while (op != 8):
        op = menu()
        if op == 1:
            agregarProducto()
        elif op == 2:
            modificarProducto()
        elif op == 3:
            buscarCod()
        elif op == 4:
            buscarNom()
        elif op == 5:
            buscarPr()
        elif op == 6:
            mostrarMinExist()
        elif op == 7:
            eliminar()
        elif op == 8:
            print("Adiós...")
        else:
            print("Opción inválida...")


main()
