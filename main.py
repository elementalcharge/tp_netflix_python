	
def probabilidad():
	#genera la cantidad de visualizaciones que le pondra al video
	
	r=random.randint(1,101)
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
	else:
	 return 0
def topSeries(lista):
	#listado de series mas vistas
	auxiliar={ 'numeroCapitulo' : '1','descCapitulo' : 'Asd','tituloCapitulo' : 'Asd','duracion' : '20','visualizaciones' : 0}
	episodioauxiliar=[auxiliar,auxiliar,auxiliar,auxiliar,auxiliar ]
	for x in lista:
		for y in x['Temporada']:
			for z in y['capitulos']:
				if z['visualizaciones']>episodioauxiliar[4]['visualizaciones']:
					episodioauxiliar[4]=z
					episodioauxiliar=sorted(episodioauxiliar,key=lambda k:k['visualizaciones'] ,reverse=True)
	for x in episodioauxiliar:
		print(x)
	
		
		
def inputUsuarioInt():
	value=False
	while value==False:
		try:
			leer=int(raw_input('ingrese numerovalido'))

		except ValueError:
			print("valor no valido. ingreseun valor valido")
		else:
			value=True
	return leer
	
def generarVisuializaciones( directorio):
	print("ingrese el numero de visualizaciones a generar")
	lim=inputUsuarioInt()
	while lim>0:
		r1=random.randint(0,len(directorio)-1)
		r2=random.randint(0,len(directorio[r1]['Temporada'])-1)
		r3=random.randint(0,len(directorio[r1]['Temporada'][r2]['capitulos'])-1)
		aux=directorio[r1]['Temporada'][r2]['capitulos'][r3]
		p=probabilidad()
		lim-=int(p)
		if(lim<0):
			aux['visualizaciones']=int(aux['visualizaciones'])+(lim+p)
		else:
			aux['visualizaciones']=int(aux['visualizaciones'])+p
	
def inputusuarioindex (array):
	inrango=False
	while  inrango== False:
		eleccion=inputUsuarioInt() 
		if(eleccion <len(array) and eleccion>=0):
			inrango=True
		else:
			print "ingrese un valor valido"
	return eleccion


		
def main():
	opcion=-1
	import reader
	listado = reader.cargar_peliculas('series.txt')
	

	while opcion != 0:

		print "1_explorador"
		print "2_generar visualizaciones"
		print "3_top series"
		print "0_salir"
		opcion= inputUsuarioInt()
		if opcion==1:
			explorador(listado)
		elif opcion==2:
			generarVisuializaciones(listado)
		elif opcion==3:
			topSeries(listado)

def explorador (directorio):
	for x in range(0,len(directorio)):
		print ("opcion{0} : {1}").format(x,directorio[x]['Serie'])
	
	eserie=inputusuarioindex(directorio)
	nombreSerie = directorio[eserie]['Serie']
	print (nombreSerie)

	for y in range (0, len(directorio[eserie]['Temporada'])):
		print ("opcion",y,"Temporada", directorio[eserie]['Temporada'][y]['numeroTemporada'])

	etemporada = inputusuarioindex(directorio[eserie]['Temporada'])


	for z in range (0,len(directorio[eserie]['Temporada'][etemporada]['capitulos'])):
		print ("Capitulo", directorio[eserie]['Temporada'][etemporada]['capitulos'][z])
		print ("Capitulo", directorio[eserie]['Temporada'][etemporada]['capitulos'][z]['tituloCapitulo'])
		print ("Capitulo", directorio[eserie]['Temporada'][etemporada]['capitulos'][z]['visualizaciones'])







if __name__ == '__main__':
	import random
	main()

		
	
