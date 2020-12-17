import Relacion
import Estado
import Automata

""" Compiladores 3CM8"""
""" Proyecto Analizador lexico """
""" Maria José Salmerón Contreras y Hugo Santiago Gomez Salas"""
""" Jose Sanchez Juarez"""


""" Declaracion del automata y su partes """


""" Declaracion de Estados """
estQ0=Estado.Estado("q0",False,[])
estQ1=Estado.Estado("q1",True,[])
estQ2=Estado.Estado("q2",True,[])
estQ3=Estado.Estado("q3",True,[])
estQ4=Estado.Estado("q4",True,[])
estQ5=Estado.Estado("q5",False,[])

""" Declaracion de relaciones """
""" relaciones q0"""
""" 0=letras 1=numeros """
relQ0_Q1=Relacion.Relacion(estQ1,["0"])
relQ0_Q5=Relacion.Relacion(estQ5,["1"])
estQ0.lstRelaciones.append(relQ0_Q1)
estQ0.lstRelaciones.append(relQ0_Q5)
""" relaciones q1"""
relQ1_Q2=Relacion.Relacion(estQ2,["0"])
relQ1_Q3=Relacion.Relacion(estQ3,["1"])
estQ1.lstRelaciones.append(relQ1_Q2)
estQ1.lstRelaciones.append(relQ1_Q3)
""" relaciones q2"""
relQ2_Q2=Relacion.Relacion(estQ2,["0"])
relQ2_Q4=Relacion.Relacion(estQ4,["1"])
estQ2.lstRelaciones.append(relQ2_Q2)
estQ2.lstRelaciones.append(relQ2_Q4)
""" relaciones q3"""
relQ3_Q2=Relacion.Relacion(estQ2,["0"])
relQ3_Q3=Relacion.Relacion(estQ3,["1"])
estQ3.lstRelaciones.append(relQ3_Q2)
estQ3.lstRelaciones.append(relQ3_Q3)
""" relaciones q4"""
relQ4_Q3=Relacion.Relacion(estQ3,["1","0"])
estQ4.lstRelaciones.append(relQ4_Q3)
""" relaciones q5"""
relQ5_Q5=Relacion.Relacion(estQ5,["0","1"])
estQ5.lstRelaciones.append(relQ5_Q5)


""" Declaracion del automata """

lstEstados=[
estQ0,
estQ1,
estQ2,
estQ3,
estQ4,
estQ5,
]

autoprueba=Automata.Automata(lstEstados,estQ0,["0","1"])

autoprueba.reduccion()