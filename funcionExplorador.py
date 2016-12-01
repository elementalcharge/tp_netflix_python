def explorador (self,directorio):
	for x in directorio(0,len(directorio)):
		print("opcion {0} :").format(x['Serie'])
		
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


