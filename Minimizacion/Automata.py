from Relacion import Relacion
from Estado import Estado

class Automata:

    def __init__(self, lstEstados, estadoI, lenguaje):
        self.lstEstados = lstEstados
        self.estadoI = estadoI
        self.EstadoA = estadoI
        self.lenguaje = lenguaje

    def evaluar(self, palabra):
        self.EstadoA = self.estadoI
        for letra in palabra:

            for relacion in self.EstadoA.lstRelaciones:

                if letra in relacion.lstChar:

                    print(self.EstadoA.nombre+"("+letra+")" +
                          "=>"+relacion.EstadoD.nombre)
                    self.EstadoA = relacion.EstadoD

                    break

        return self.EstadoA.aceptacion

    def tablaDeClases(self,clases):
        estados=self.estadosAautomata(clases)

        relacionMatrix = {}
        for estado in estados:
            lstTrans = {}

            for letra in self.lenguaje:

                for relacion in estado.lstRelaciones:

                    if letra in relacion.lstChar:

                        lstTrans[letra] = relacion.EstadoD.nombre
                        break

            relacionMatrix[estado.nombre] = lstTrans

        return relacionMatrix

    def tablaTransicion(self):
        relacionMatrix = {}
        for estado in self.lstEstados:
            lstTrans = {}

            for letra in self.lenguaje:

                for relacion in estado.lstRelaciones:

                    if letra in relacion.lstChar:

                        lstTrans[letra] = relacion.EstadoD.nombre
                        break

            relacionMatrix[estado.nombre] = lstTrans

        return relacionMatrix

    def reduccion(self):
        tablaoriginal = self.tablaTransicion()
        lstEliminados = self.lstEstados[:]
        print(tablaoriginal)

        for estado in self.lstEstados:

            lstDestinos = tablaoriginal[estado.nombre]

            for letra in self.lenguaje:

                for estadoComp in self.lstEstados:
                    if  estadoComp in lstEliminados and (lstDestinos[letra] == estadoComp.nombre or estadoComp.nombre == self.estadoI.nombre):

                        lstEliminados.remove(estadoComp)

        for estadoElim in lstEliminados:
            self.lstEstados.remove(estadoElim)

        lstAceptados = []
        lstDenegados = []

        for estado in self.lstEstados:

            if estado.aceptacion:

                lstAceptados.append(estado)

            else:

                lstDenegados.append(estado)

        AutomataBase = {
            "c1": lstDenegados,
            "c2": lstAceptados
        }

        nuevosEstados = self.simplificacion(AutomataBase)

        self.lstEstados=self.estadosAautomata(nuevosEstados)

        tablaFinal=self.tablaTransicion()

        print(tablaFinal)

    def estadosAautomata(self,clases :dict):
        lstNuevosEstados=[]
        for clase in clases:
            estadoMuestra=clases[clase][0]
            nuevoestado=Estado(clase,estadoMuestra.aceptacion,[])
            lstNuevosEstados.append(nuevoestado)
        i=0
        for clase in clases: 
            lstaRelaciones=[]
            estadoMuestra=clases[clase][0]
            for relacion in estadoMuestra.lstRelaciones:
                for claseDestino in clases:
                    if relacion.EstadoD in clases[claseDestino]:
                        estadoDestino=relacion.EstadoD
                        for nuevos in lstNuevosEstados:
                            if nuevos.nombre==claseDestino:
                                estadoDestino=nuevos
                        lstaRelaciones.append(Relacion(estadoDestino,relacion.lstChar))
            for rel in lstaRelaciones:
                lstNuevosEstados[i].lstRelaciones.append(rel)
            i+=1
        return lstNuevosEstados

    def simplificacion(self, clases):
        nuevasClases = {}
        for clase in clases:

            lstestados = clases[clase]

            for estado in lstestados:

                clasesDestino = "c"

                for letra in self.lenguaje:

                    for transicion in estado.lstRelaciones:

                        if letra in transicion.lstChar:

                            estadoDestino = transicion.EstadoD
                            for claseD in clases:

                                if estadoDestino in clases[claseD]:

                                    clasesDestino += claseD.replace("c", "")
                                    break
                            break
                if estado.aceptacion:
                    if clase in nuevasClases.keys():
                        nuevasClases[clase].append(estado)
                    else:
                        nuevasClases[clase] = [estado]
                else:
                    if clasesDestino in nuevasClases.keys():
                        nuevasClases[clasesDestino].append(estado)

                    else:
                        nuevasClases[clasesDestino] = [estado]

        if len(nuevasClases.keys()) > len(clases.keys()):

            for clase in nuevasClases:
                claseContent=""
                i=0
                for estado in nuevasClases[clase]:

                    if i==0:
                        claseContent+=clase+"{"
                    if i==len(nuevasClases[clase])-1:
                        claseContent+=estado.nombre+"}"
                    else:
                        claseContent+=estado.nombre+","
                    i+=1
                print(claseContent)
            print(self.tablaDeClases(nuevasClases))

            return self.simplificacion(nuevasClases)

        else:

            for clase in nuevasClases:
                claseContent=""
                i=0
                for estado in nuevasClases[clase]:

                    if i==0:
                        claseContent+=clase+"{"
                    if i==len(nuevasClases[clase])-1:
                        claseContent+=estado.nombre+"}"
                    else:
                        claseContent+=estado.nombre+","
                    i+=1
                print(claseContent)
            print(self.tablaDeClases(nuevasClases))

            return nuevasClases
