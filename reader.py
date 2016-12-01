def cargar_peliculas(nombre_archivo):
	"""esta funcion se encarga de leer el archivo en donde estan cargadas todas las peliculas y retorna una estructura de datos con todas las peliculas almacenadas en ella"""

	def leer_archivo(archivo):
		"""lee el archivo"""
		from csv import reader
		try:
			ads = reader(archivo)
		except IOError:
			pass
		row = next(ads)
		return row

	file = open(nombre_archivo,"rb")
	leer_archivo(file) #para saltear los datos del header

	serie, Desc, temporada, anio, capitulo, descptCap, titulo, durac, vis, eof  = leer_archivo(file)
	lCapitulos = []
	lTemporadas = []
	lSeries = []
	while eof != "True":
		serie_anterior = serie
		desc_anterior = Desc

		#Primer corte de control
		while serie_anterior == serie and eof != "True":
			temporada_anterior = temporada
			anio_anterior = anio

			#Segundo corte de control
			while  serie_anterior == serie and temporada_anterior == temporada and eof != "True":
				
				
				dCapitulos = dict([("numeroCapitulo",capitulo), ("descCapitulo",descptCap), ("tituloCapitulo",titulo), ("duracion",durac), ("visualizaciones",vis)])
				lCapitulos.append(dCapitulos)
				serie, Desc, temporada, anio, capitulo, descptCap, titulo, durac, vis, eof  = leer_archivo(file)	
				
			dTemporadas = dict([("numeroTemporada",temporada_anterior), ("anoEmision",anio_anterior), ("capitulos",lCapitulos)])
			lTemporadas.append(dTemporadas)
			lCapitulos = []

		dSerie = dict([("Serie", serie_anterior) , ("descSerie",desc_anterior), ("Temporada", lTemporadas)])
		lSeries.append(dSerie)
		lTemporadas = []
	
	file.close()
	return lSeries




def crear_usuario(nombre,apellido):
	return "%s, %s" % (nombre, apellido)

