def topSeries(lista):
	episodioauxiliar=[{ 'numeroCapitulo' : '1',
                                     'descCapitulo' : 'Asd',
                                     'tituloCapitulo' : 'Asd',
                                     'duracion' : '20',
                                     'visualizaciones' : 0,
                                     'serie' : 'ninguna',
                                     'Temporada': 0
                                     } for i in range(0,5)]
	for x in lista:
		for y in range(0,len(x.Temporada)):
			for z in range(0,len(x.Temporada[y][z])):
				if x['temporada'][y]['capitulos'][z] > episodioauxiliar[4]['visualizaciones']:
					episodioauxiliar[4]=x.Temporada[y].Capitulo[z]
					sorted(episodioauxiliar,key=lambda k:k['visualizaciones'] ,reverse=True )
	for x in episodioauxiliar:
		print(x)
		
	
def probabilidad(self):
	import random
	r=random.uniform(1,100)
	if(r>=60 and r<80):

		return 1
	elif(r>=80 and r<90):
		return 2

	elif(r>=90 and r<95):
		return 3

	elif(r>=95 and r<98):
		return 4

	elif(r>=98 and r<99):
		return 5

	elif(r>=99 and r<100):
		return 150
	
def inputUsuarioInt():
	value=False
	while value==False:
		try:
			leer=int(raw_input('ingrese visualizaciones a generar'))

		except ValueError:
			print("valor no valido. ingreseun valor valido")
			pass
		else:
			value=True
	return leer
	
def generarVisuializaciones(self, directorio):
		
	max=inputUsuarioInt()
	while max>0:
		aux=directorio[random(0,len(directorio))]
		aux2=aux.temporada[random(0,len(aux.temporada))]
		aux3=aux2.capitulo[random(0,len(aux2.capitulo))]
		p=probabilidad()
		max-=p
		if(max>=0):
			aux3.visualizaciones+=p
		elif(max<0):
			aux3.visualizaciones+=(max+p)
	
def inputusuarioindex (self,array):

		inrango = False

		while inrango == False:

			eleccion = inputUsuarioInt() 
			if( eleccion < len(array) and eleccion>=0):
				inrango=True
			else:
				print("ingrese un valor valido")
		return eleccion

def explorador (self,directorio):
	for x in directorio(0,len(directorio)):
		print("opcion {0} :").format(x)
		directorio[x].Serie
		
	eserie=inputusuarioindex(directorio)
	print (directorio[eserie].serie)

	for y in range (0, len(directorio[eserie].Temporada)):
		print ("opcion",y,"Temporada", directorio[eserie].Temporada[y].numeroTemporada)

	etemporada= inputusuarioindex(directorio[eserie].Temporada)


	for z in range (0,len(directorio[eserie].Temporada[etemporada].capitulos)):
		print ("Capitulo", directorio[eserie].Temporada[etemporada].capitulos[z].numeroCapitulo)
		print ("Capitulo", directorio[eserie].Temporada[etemporada].capitulos[z].tituloCapitulo)
		print ("Capitulo", directorio[eserie].Temporada[etemporada].capitulos[z].visualizaciones)


		
def main():
	opcion=-1

	while opcion != 0:

		print "1_explorador"
		print "2_generar visualizaciones"
		print "3_top series"
		print "0_salir"
		opcion= inputUsuarioInt()
		if opcion==1:
			explorador()
		elif opcion==2:
			generarVisuializaciones()
		elif opcion==3:
			topSeries()


		





if __name__ == '__main__':
	main()

		
