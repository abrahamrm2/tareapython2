precio = input("Introduce el precio del producto en euros (con dos decimales): ")
euros, centimos = precio.split('.')
print(f"Número de euros: {euros}, Número de céntimos: {centimos}")
