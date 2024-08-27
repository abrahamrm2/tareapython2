fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
dia, mes, anio = fecha.split('/')
print(f"Día: {dia.zfill(2)}, Mes: {mes.zfill(2)}, Año: {anio}")
