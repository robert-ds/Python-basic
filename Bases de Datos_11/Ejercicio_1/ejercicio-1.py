# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
import sqlite3

def insertAlumnos():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        '''INSERT INTO alumnos(id,nombre,apellido) 
        VALUES
        (2,"Pastor","almeida"), 
        (3,"Victor","Perez"),
        (4,"José","Guevara"),
        (5,"Juan","Campos"),
        (6,"Jimmy","Carry"),
        (7,"John","Elthon"),
        (8,"Jackie","Chan"),
        (9,"Robert","Dniro")'''
    )

    conn.commit()
    cursor.close()
    conn.close()

def buscaAlumno(nombre):
    conn = sqlite3.connect('data.db')                                                                                                                 
    cursor = conn.cursor()
    
    rows = cursor.execute(f"SELECT nombre FROM alumnos WHERE nombre='{nombre}' LIMIT 1")
    alumno = rows.fetchone()[0]

    if nombre == alumno:
        print("Nombre del alumno: ",alumno)
    else:
        print("El alumno no Existe")
    
    cursor.close()
    conn.close()

def main():
    #insertAlumnos()
    buscaAlumno('Jimmy')



if __name__ == "__main__":
    main()
    
