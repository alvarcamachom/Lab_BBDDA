import random
import csv

# Lista de géneros
generos = ["Acción", "Aventura", "Comedia", "Drama", "Fantasía", "Ciencia Ficción", "Romance", "Terror", "Misterio", "Animación", "Documental", "Crimen", "Histórica", "Musical", "Guerra", "Western", "Deportes", "Familiar", "Suspense", "Biográfica"]

# Lista de idiomas
idiomas = ["EN", "ES", "FR", "DE", "IT", "PT", "CN", "JP", "KR", "RU", "AR", "HI", "SW", "NL", "PL", "TR", "VI", "ID", "TH", "FI", "NO", "SV", "DA", "HU", "CS", "RO", "EL", "UK", "FA", "HE"]

# Lista de nacionalidades
nacionalidades = ["Español", "Inglés", "Francés", "Alemán", "Italiano", "Portugués", "Chino", "Japonés", "Coreano", "Ruso", "Árabe", "Hindi", "Swahili", "Holandés", "Polaco", "Turco", "Vietnamita", "Indonesio", "Tailandés", "Finlandés", "Noruego", "Sueco", "Danés", "Húngaro", "Checo", "Rumano", "Griego", "Ucraniano", "Persa", "Hebreo"]

# Lista de nombres
nombres = ["Juan", "María", "Pedro", "Ana", "Carlos", "Laura", "Jorge", "Sofía", "Diego", "Isabel", "Luis", "Elena", "Fernando", "Valeria", "Andrés", "Camila", "Ricardo", "Gabriela", "Francisco", "Daniela", "Mario", "Carla", "José", "Paula", "Miguel", "Catalina", "Raul", "Pamela", "Raúl", "Natalia", "Gustavo", "Verónica", "Pablo", "Renata", "Alejandro", "Lucía", "Fabián", "Beatriz", "Hernán", "Marcela", "Roberto", "Patricia", "Rodrigo", "Silvia", "Esteban", "Concepción", "Javier", "Adriana", "Ernesto", "Montserrat", "Simón", "Rosa", "Emilio", "Mónica", "Arturo", "Juana", "Martín", "Carmen", "Guillermo", "Josefina"]

#Lista de comentarios
comentarios = ["Emocionante de principio a fin.","Efectos visuales asombrosos.","Actuaciones increíbles.","Trama intrigante con giros sorprendentes.","Efectos de sonido realistas.", "Mantiene al borde del asiento.", "Personajes entrañables y conmovedores.", "Reflexión sobre la vida.","Cinematografía impresionante.","Imperdible en la pantalla grande.","Dirección impecable.","Deja con ganas de más."]




def generador_peliculas(archivo):
    with open ('Pelicula.txt' , "w") as archivo_peli_csv:
        archivo_peli_csv.write("año,titulo,duracion,idioma,calificacion\n")
        for i in range (400000):
               # Año de la película entre 1950 y 2023
                año = random.randint(1950, 2023)
                #Titulo 
                titulo= 'Pelicula numero: '+ str(i)
                # Duración de la película entre 90 y 240 minutos
                duracion = random.randint(90, 240)
                # Idioma de la película entre 1 y 30
                idioma = random.choice(idiomas)
                # Calificación de la película entre 0 y 10 
                calificacion = random.randint(0, 10)                 
                codigo = i
                archivo_peli_csv.write(f"{año},{titulo},{duracion},{idioma},{calificacion}\n")
#archivo_peli_csv.close()
generador_peliculas(archivo='Pelicula.txt')
      

def generador_persona(archivo1):
     with open ('Persona.txt' , "w") as archivo_person_csv:
         #cabecera de csv
         archivo_person_csv.write("año,nombre,nacionalidad\n")  
         for i in range(400000):
        #Fecha de nacimiento entre 1950 y 2020
        # dia_nacimiento= random.randint(1, 31)
        # mes_nacimiento= random.randint(1, 12)
            año_nacimiento = random.randint(1950,2020)
            #Nombre
            nombre = random.choice(nombres)
            #Nacionalidad de la persona 
            nacionalidad = random.choice(nacionalidades)
            archivo_person_csv.write(f"{año_nacimiento},{nombre},{nacionalidad}\n")
#archivo_person_csv.close()
generador_persona('Persona.txt')



def generador_criticas(archivo):
     with open ('Critica.txt' , "w") as archivo_critica_csv:
         #cabecera
         archivo_critica_csv.write("Puntuacion,Fecha,Texto\n") 
         num_criticas = random.randint(1, 100)
         for i in range(num_criticas):
             # Fecha de las críticas (año 2022, día y mes aleatorios)
            dia_criticas = random.randint(1, 31)
            mes_criticas = random.randint(1, 12)
            año_criticas = int(2022)
            # Puntuación de las críticas (entre 0 y 10)
            puntuacion_criticas = random.randint(0,10)
            texto= random.choice(comentarios)
            archivo_critica_csv.write(f"{dia_criticas},{mes_criticas},{año_criticas},{puntuacion_criticas},{texto}\n")
#archivo_critica_csv.close()
generador_criticas(archivo='Critica.txt')


def generador_visualizaciones(archivo):
    with open ('Visualizacion.txt' , "w") as archivo_visualizacion_csv:
         #cabecera
        archivo_visualizacion_csv.write("Fecha\n")    
         #Número de visualizaciones varia entre 1 y 100
        num_visualizacion= random.randint(1,100)
        for i in range(num_visualizacion):
            dia_visualizacion = random.randint(1, 31)
            mes_visualizacion= random.randint(1, 12)
            año_visualizacion = int(2022)
            archivo_visualizacion_csv.write(f"{dia_visualizacion},{mes_visualizacion},{año_visualizacion}\n")
#archivo_visualizacion_csv.close()
generador_visualizaciones(archivo='Visualizacion.txt')



def generador_generos(archivo):
     with open ('Generos.txt',"w") as archivo_generos_csv:            
        num_generos=random.randint(1,6)
        genero=[]
        for i in range(num_generos): 
                        if i!=(num_generos-1):
                            genero+=random.choice(generos)+ ","
                        else:
                            genero+=random.choice(generos)
        archivo_generos_csv.write(f"{genero}\n")
#archivo_generos_csv.close()
generador_generos(archivo ='Generos.txt')
        