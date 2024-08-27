correo = input("Introduce tu correo electrónico: ")
nombre, dominio = correo.split('@')
nuevo_correo = f"{nombre}@ceu.es"
print(nuevo_correo)
