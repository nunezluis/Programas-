# programa para evaluar tareas y examenes eligiendo al azar entre una lista de estudiantes y una lista de preguntas
import random
# funcion para generar aleatoriamente los estudiantes y las preguntas
def QuienPasa(NumAlumnos, NumPreguntas, NumItems):
    Alumno = random.randint(1,NumAlumnos)
    Pregunta =  random.randint(1,NumPreguntas)
    Item =  random.randint(1,NumItems)
    return Alumno, Pregunta, Item
#
# funcion que hace una pregunta y valida que la respuesta sea s o n
def ValidaPreguntaSN(QuePregunto):
    respuesta = "w"
    while (respuesta != "s") and (respuesta != "n"):
        respuesta = raw_input(QuePregunto+" (s,n)")
    return respuesta
#
# funcion para determinar si hay un elemento repetido en una lista
def ElementoRepetido(Lista, TamanoLista, Elemento):
    z=0
    while z < TamanoLista:
#        print z, Lista,TamanoLista,Elemento
        if Lista[z] == Elemento:
            repetido = "s"
#            print z
            break
        else:
            repetido = "n"
        z = z+1
    return repetido
#
#
# Comienzo del programa
QuePregunto = "Termino la evaluacion?"
#
# Pregunto por el numero de estudianes y armo una lista para almacenar los evaluados
NumAlumnos = input("Numero de estudiantes ? ")
i = 1
AlumnosEvaluados = [0]
while i <= NumAlumnos-1:
    AlumnosEvaluados.append(0)
    i = i +1
#
# pregunto por el numero de preguntas y armo otra lista para almacenar las evaluadas
NumPreguntas = input("Numero de preguntas de la tarea ? ")
i = 1
PreguntasEvaluadas = [0]
while i <= NumPreguntas-1:
    PreguntasEvaluadas.append(0)
    i = i +1
#
# Pregunto por el numero maximo de items
NumItems = input("Numero maximo de apartados por pregunta ? ")
#
# defino valores iniciales de algunas variables
k, j, Alumno, respuesta = 0, 0, 0, "n"
#
# mientras no se acabe la evaluacion o los estudiantes o las preguntas
while  (k < NumAlumnos) and (respuesta == "n") and (j < NumPreguntas):
# genero alumnos y preguntas al azar
    Alumno, Pregunta, Item = QuienPasa(NumAlumnos, NumPreguntas, NumItems)
# chequeo que las preguntas y los alumnos no hayan sido evaluados anterioremente
    AlumnoRepetido = ElementoRepetido(AlumnosEvaluados, k+1, Alumno)
    PreguntaRepetida = ElementoRepetido(PreguntasEvaluadas, j+1, Pregunta)
    if AlumnoRepetido == "s" or PreguntaRepetida == "s":
        pass
    else: # Si no han sido evaluadas y evaluados los anuncio y los almanceno en una lista
        AlumnosEvaluados[k]=Alumno
        PreguntasEvaluadas[j] = Pregunta
        print "Estudiante Num:", AlumnosEvaluados[k],"   Pregunta Num:", PreguntasEvaluadas[j], "   Apartado Num:", Item
        respuesta = ValidaPreguntaSN(QuePregunto)
        k=k+1
        j=j+1
print  "gracias"
