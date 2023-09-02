nomes = ['ana', 'larissa', 'carlos', 'crsitina', 'maria', 'jonas', 'mário']
genero = {'ana': 'f', 'larissa': 'f', 'carlos': 'm', 'crsitina': 'f', 'maria': 'f', 'jonas': 'm', 'mário': 'm'}
s = [f"Sr. {nome}" if genero[nome] == 'm' else f"Sra. {nome}" for nome in nomes]
print(s)