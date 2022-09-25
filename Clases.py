class producto:
    def __init__(self, cod, name, desc, prc, exis, minExis):
        self.Codigo = cod
        self.Nombre = name
        self.Descripcion = desc
        self.Precio = prc
        self.Existencia = exis
        self.ExistenciaMinima = minExis

    def __str__(self):
        return f"""
        Código: {self.Codigo}
        Nombre: {self.Nombre}
        Descripcion: {self.Descripcion}
        Precio: {self.Precio}
        Existencia: {self.Existencia}
        Existencia mínima: {self.ExistenciaMinima}"""


class ListaProd:
    def __init__(self):
        self.listaP = []

    def agregar(self, elemento):
        try:
            self.listaP.append(elemento)
        except Exception as ex:
            print("Ocurrio un error al agregar el producto", str(ex))

    def editar(self, elemento, pos):
        try:
            self.listaP[pos] = elemento
        except Exception as ex:
            print("Ocurrio un error al modificar el producto", str(ex))

    def buscarPorCodigo(self, cod):
        try:
            pos = 0
            for prod in self.listaP:
                if prod.Codigo == cod:
                    return prod, pos
            pos += 1
        except Exception as ex:
            print("Ocurrio un error al buscar el codigo", str(ex))

    def buscarPorNombre(self, name):
        try:
            pos = 0
            for prod in self.listaP:
                if prod.Nombre == name:
                    return prod, pos
            pos += 1
        except Exception as ex:
            print("Ocurrio un error al buscar el nombre", str(ex))

    def buscarPorPrecio(self, prc):
        try:
            pos = 0
            for prod in self.listaP:
                if prod.Precio == prc:
                    return prod, pos
            pos += 1
        except Exception as ex:
            print("Ocurrio un error al buscar el precio", str(ex))

    def buscarExistenciaMin(self):
        try:
            pos = 0
            for prod in self.listaP:
                if prod.Existencia < prod.ExistenciaMinima:
                    print(prod)
            pos += 1
        except Exception as ex:
            print("Ocurrio un error al buscar motrar los productos", str(ex))

    def eliminar(self, prod):
        try:
            self.listaP.remove(prod)
        except Exception as ex:
            print("Ocurrio un error al eliminar el producto", str(ex))
