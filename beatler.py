import os, collections, csv
 
#Rutas
ruta = '../Amonjerro/Destination Beatles/'
de_ruta ='../Amonjerro/Beatles/'
 
#Variables
lista_discos = os.listdir(ruta)
contador = collections.Counter()
total_de_palabras = 0
total_de_archivos = 0
puntuacion = ['.','"',',',';','(',')','!','?','[',']']
 
#Limpiar archivos
for i in lista_discos:
    lista_canciones = os.listdir(ruta+i)
    for j in lista_canciones:
        with open(de_ruta+i+'/'+j,'r') as f:
            r = f.read()
            for punt in puntuacion:
                r = r.replace(punt,'')
            r = r.replace('-',' ')
            r = r.lower()
            f.close()
        f = open(ruta+i+'/'+j,'w')
        f.write(r)
        f.close()
 
#Realizar los conteos
for i in lista_discos:
    lista_canciones = os.listdir(ruta+i)
    for j in lista_canciones:
        total_de_archivos += 1
        with open(ruta+i+'/'+j,'r') as f:
            for linea in f:
                l = linea.split()
                total_de_palabras += len(l)
                for palabra in l:
                    contador[palabra] += 1
        f.close()
 
print('Archivos: ',total_de_archivos)
print('Total Palabras: ',total_de_palabras)
print('Palabras Individuales: ', len(contador.keys()))
 
#Grabar resultados en un archivo CSV.
with open(ruta+'results.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for key in contador.keys():
        csv_writer.writerow([key,contador[key]])
    csv_file.close()
 
print('Resultados Tabulados en CSV')