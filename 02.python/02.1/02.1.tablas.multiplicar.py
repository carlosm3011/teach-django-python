# Tablas de multiplicar v2

bases = range(1,12)

def calc_tabla_multiplicar(base, nmax):
	res = {'base': base}
	for n in range(0, nmax):
		r1 = base * n
		res[n] = r1
	# end for
	return res
# end def 

def pretty_print_tabla_multiplicar(tabla):
	print(" ")
	print(f"===Tabla del {tabla['base']}")
	for k in tabla.keys():
		if k != 'base':
			print(f"{k} * {tabla['base']} = {tabla[k]}")
		# end if
	# end for
# end def

## MAIN
if __name__ == "__main__":
	print("Tablas de multiplicar, pero ahora todas juntas")
	
	for b in bases:
		t1 = calc_tabla_multiplicar(b,12)
		pretty_print_tabla_multiplicar(t1)
	# end for

# end MAIN
