from sys import argv

script, filename = argv
# abre el archivo a leer y guarda su referencia en la variable txt
txt = open(filename)

print "Here's your file %r:" % filename

#Lee el archivo e imprime su contenido
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
