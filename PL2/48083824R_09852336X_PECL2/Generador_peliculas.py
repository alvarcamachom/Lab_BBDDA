#Programa para generar datos aleatorios para una base de datos de peliculas
#Se guardaran en un archivo csv

#importacion
import random
import csv

#Listas de datos
generos = ['Genero1', 'Genero2', 'Genero3', 'Genero4', 'Genero5', 'Genero6', 'Genero7', 'Genero8', 'Genero9', 'Genero10', 'Genero11', 'Genero12', 'Genero13', 'Genero14', 'Genero15', 'Genero16', 'Genero17', 'Genero18', 'Genero19', 'Genero20']
idiomas = ['EN', 'ES', 'DE', 'JP', 'FR', 'IT', 'PT', 'RU', 'CN', 'KR', 'AR', 'TR', 'PL', 'NL', 'SV', 'DA', 'FI', 'NO', 'CS', 'HU', 'FT', 'EL', 'HE', 'JA', 'RO', 'TH', 'VI', 'ZH', 'BG', 'HR']
nacionalidades = ['España', 'Nacionalidad2', 'Nacionalidad3', 'Nacionalidad4', 'Nacionalidad5', 'Nacionalidad6', 'Nacionalidad7', 'Nacionalidad8', 'Nacionalidad9', 'Nacionalidad10', 'Nacionalidad11', 'Nacionalidad12', 'Nacionalidad13', 'Nacionalidad14', 'Nacionalidad15', 'Nacionalidad16', 'Nacionalidad17', 'Nacionalidad18', 'Nacionalidad19', 'Nacionalidad20', 'Nacionalidad21', 'Nacionalidad22', 'Nacionalidad23', 'Nacionalidad24', 'Nacionalidad25', 'Nacionalidad26', 'Nacionalidad27', 'Nacionalidad28', 'Nacionalidad29', 'Nacionalidad30', 'Nacionalidad31', 'Nacionalidad32', 'Nacionalidad33', 'Nacionalidad34', 'Nacionalidad35', 'Nacionalidad36', 'Nacionalidad37', 'Nacionalidad38', 'Nacionalidad39', 'Nacionalidad40', 'Nacionalidad41', 'Nacionalidad42', 'Nacionalidad43', 'Nacionalidad44', 'Nacionalidad45', 'Nacionalidad46', 'Nacionalidad47', 'Nacionalidad48', 'Nacionalidad49', 'Nacionalidad50', 'Nacionalidad51', 'Nacionalidad52', 'Nacionalidad53', 'Nacionalidad54', 'Nacionalidad55', 'Nacionalidad56', 'Nacionalidad57', 'Nacionalidad58', 'Nacionalidad59', 'Nacionalidad60', 'Nacionalidad61', 'Nacionalidad62', 'Nacionalidad63', 'Nacionalidad64', 'Nacionalidad65', 'Nacionalidad66', 'Nacionalidad67', 'Nacionalidad68', 'Nacionalidad69', 'Nacionalidad70', 'Nacionalidad71', 'Nacionalidad72', 'Nacionalidad73', 'Nacionalidad74', 'Nacionalidad75', 'Nacionalidad76', 'Nacionalidad77', 'Nacionalidad78', 'Nacionalidad79', 'Nacionalidad80', 'Nacionalidad81', 'Nacionalidad82', 'Nacionalidad83', 'Nacionalidad84', 'Nacionalidad85', 'Nacionalidad86', 'Nacionalidad87', 'Nacionalidad88', 'Nacionalidad89', 'Nacionalidad90', 'Nacionalidad91', 'Nacionalidad92', 'Nacionalidad93', 'Nacionalidad94', 'Nacionalidad95', 'Nacionalidad96', 'Nacionalidad97', 'Nacionalidad98', 'Nacionalidad99', 'Nacionalidad100']
nombres = ['Marta', 'Paco', 'Antonio', 'Pepe', 'Mario', 'Juan', 'Jose', 'Maria', 'Luis', 'Luisa', 'Rosa', 'Ramo', 'Ramon', 'Ana', 'Andres', 'Andrea', 'Sara', 'Steven', 'Perez', 'Guille', 'Guillermo', 'Guillen', 'Martin', 'Alberto', 'Oriol', 'Valeria', 'Candido', 'Matiz', 'Miguel', 'Miguelito', 'Miguelina', 'Miguelon', 'Migas']
comentarios = ['Comentario1', 'Comentario2', 'Comentario3', 'Comentario4', 'Comentario5', 'Comentario6', 'Comentario7', 'Comentario8', 'Comentario9', 'Comentario10']
titulos = ['Titulo1', 'Titulo2', 'Titulo3', 'Titulo4', 'Titulo5', 'Titulo6', 'Titulo7', 'Titulo8', 'Titulo9', 'Titulo10', 'Titulo11', 'Titulo12', 'Titulo13', 'Titulo14', 'Titulo15', 'Titulo16', 'Titulo17', 'Titulo18', 'Titulo19', 'Titulo20', 'Titulo21', 'Titulo22', 'Titulo23', 'Titulo24', 'Titulo25', 'Titulo26', 'Titulo27', 'Titulo28', 'Titulo29', 'Titulo30', 'Titulo31', 'Titulo32', 'Titulo33', 'Titulo34', 'Titulo35', 'Titulo36', 'Titulo37', 'Titulo38', 'Titulo39', 'Titulo40', 'Titulo41', 'Titulo42', 'Titulo43', 'Titulo44', 'Titulo45', 'Titulo46', 'Titulo47', 'Titulo48', 'Titulo49', 'Titulo50', 'Titulo51', 'Titulo52', 'Titulo53', 'Titulo54', 'Titulo55', 'Titulo56', 'Titulo57', 'Titulo58', 'Titulo59', 'Titulo60', 'Titulo61', 'Titulo62', 'Titulo63', 'Titulo64', 'Titulo65', 'Titulo66', 'Titulo67', 'Titulo68', 'Titulo69', 'Titulo70', 'Titulo71', 'Titulo72', 'Titulo73', 'Titulo74', 'Titulo75', 'Titulo76', 'Titulo77', 'Titulo78', 'Titulo79', 'Titulo80', 'Titulo81', 'Titulo82', 'Titulo83', 'Titulo84', 'Titulo85', 'Titulo86', 'Titulo87', 'Titulo88', 'Titulo89', 'Titulo90', 'Titulo91', 'Titulo92', 'Titulo93', 'Titulo94', 'Titulo95', 'Titulo96', 'Titulo97', 'Titulo98', 'Titulo99', 'Titulo100', 'Titulo101', 'Titulo102', 'Titulo103', 'Titulo104', 'Titulo105', 'Titulo106', 'Titulo107', 'Titulo108', 'Titulo109', 'Titulo110', 'Titulo111', 'Titulo112', 'Titulo113', 'Titulo114', 'Titulo115', 'Titulo116', 'Titulo117', 'Titulo118', 'Titulo119', 'Titulo120', 'Titulo121', 'Titulo122', 'Titulo123', 'Titulo124', 'Titulo125', 'Titulo126', 'Titulo127', 'Titulo128', 'Titulo129', 'Titulo130', 'Titulo131',]

def hasta_que_dia_se_puede(month,bisiesto): #Para evitar errores de fechas
  mes_treinta_y_uno = [1,3,5,7,8,10,12]
  mes_treinta = [4,6,9,11]
  for i in mes_treinta_y_uno:
    if month == i:
      return (31)
  for i in mes_treinta:
    if month == i:
      return (30)
  if bisiesto and month == 2:
    return (29)
  else:
    return (28)
    
def es_bisiesto (year):
    return ((year%4 == 0 and not year%100==0) or (year%100 == 0 and year % 400 == 0))


def hay_duplicado(array_que_miramos,valor_que_miramos):
  duplicado = False
  for k in array_que_miramos:
    if k == valor_que_miramos:
      duplicado = True
  return duplicado


def generar_personas(archivo): # ********************************************************************************************************************************************************
    #Guardar en un archivo csv
    with open('personasRandom.csv', "w") as archivo_csv:
        for i in range(1,400001):
            #generar datos aleatorios
            codigo_personas = i
            nombre = random.choice(nombres)
            año_nacimiento = random.randint(1950, 2020)
            mes = random.randint(1, 12)
            dia = random.randint(1, hasta_que_dia_se_puede(mes, es_bisiesto(año_nacimiento))) 
            fecha_nacimiento = f'{dia}/{mes}/{año_nacimiento}' 
            nacionalidad = random.choice(nacionalidades)
            #escribirlos en el archivo
            archivo_csv.write(f'{nombre},{nacionalidad},{fecha_nacimiento},{codigo_personas}\n')
    print('Personas Generadas')

generar_personas(archivo='personasRandom.csv')

def generar_pelicula(archivo): # ********************************************************************************************************************************************************
    #Guardar en un archivo csv
    with open('peliculasRandom.csv', "w") as archivo_csv:
        for i in range(1,400001):
            #generar datos aleatorios
            codigo_pelicula = i
            año = random.randint(1950, 2023)
            titulo = random.choice(titulos)
            idioma = random.choice(idiomas)
            calificacion = random.randint(0, 10)
            duracion = random.randint(90, 240)
            codigo_director = random.randint(1, 400000) #como hay 400000 personas, el codigo de la persona sera el numero aleatorio de una de ellas
            #escribirlos en el archivo
            archivo_csv.write(f'{año},{titulo},{duracion},{idioma},{calificacion},{codigo_pelicula},{codigo_director}\n')
    print('Peliculas Generadas')

generar_pelicula(archivo='peliculasRandom.csv')

def generar_generos(archivo): # ARREGLADO?
    #Guardar en un archivo csv
    with open('generosRandom.csv', "w") as archivo_csv:
        for j in range(1,400001):
            num_generos = random.randint(1,6)
            generos_ya_puestos = []
            for i in range(num_generos):
                genero = random.choice(generos)
                if (len(generos_ya_puestos) == 0):
                    generos_ya_puestos.append(genero)
                else:
                    while (hay_duplicado(generos_ya_puestos,genero)):
                        genero = random.choice(generos)
                    generos_ya_puestos.append(genero)
            for k in range(len(generos_ya_puestos)):
                archivo_csv.write(f'{generos_ya_puestos[k]},{j}\n')
    print('Generos Generados')

generar_generos(archivo='generosRandom.csv')

def generar_criticas(archivo): # ********************************************************************************************************************************************************
    #Guardar en un archivo csv
    with open('criticasRandom.csv', "w") as archivo_csv:
        for j in range(1,400001):
            #codigo_pelicula es j
            #codigo_persona es aleatorio entre 1 y 400000?
            num_criticas = random.randint(1,100)
            personas_que_critican = []
            for k in range(num_criticas):
                  codigo_personas_generado = random.randint(1, 400000)
                  if (len(personas_que_critican) == 0):
                    personas_que_critican.append(codigo_personas_generado)
                  else:
                    while (hay_duplicado(personas_que_critican,codigo_personas_generado)):
                      codigo_personas_generado = random.randint(0, 400000)
                    personas_que_critican.append(codigo_personas_generado)
            for i in range(num_criticas):
                #generar datos aleatorios
                puntuacion = random.randint(0, 10)
                año = 2022
                mes = random.randint(1, 12)
                dia = random.randint(1, hasta_que_dia_se_puede(mes, False))  #Para evitar errores de fechas
                fecha = f'{dia}/{mes}/{año}' 
                comentario = random.choice(comentarios)
                codigo_pelicula_peliculas = j
                codigo_personas_personas = personas_que_critican[i]                
                #escribirlos en el archivo
                archivo_csv.write(f'{puntuacion},{comentario},{fecha},{codigo_pelicula_peliculas},{codigo_personas_personas}\n')
    print('Criticas Generadas')

generar_criticas(archivo='criticasRandom.csv')

def generar_visualizaciones (archivo): # ARREGLAR
    #Guardar en un archivo csv
    with open('visualizacionesRandom.csv', "w") as archivo_csv:
        for j in range (1,400001):
            num_visualizaciones = random.randint(1,100)
            for i in range(num_visualizaciones):
                #generar datos aleatorios
                año = 2022
                mes = random.randint(1, 12)
                dia = random.randint(1, hasta_que_dia_se_puede(mes, False))  #Para evitar errores de fechas
                fecha = f'{dia}/{mes}/{año}'
                codigo_personas_generado = random.randint(1, 400000) 
                #escribirlos en el archivo
                archivo_csv.write(f'{fecha},{codigo_personas_generado},{j}\n')
    print('Visualizaciones Generadas')

generar_visualizaciones(archivo='visualizacionesRandom.csv')