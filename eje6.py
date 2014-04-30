x = "Hay %d tipos de personas." % 10
binary = "binario"
do_not = "No"
y = "Esos quienes saben %s y esos quienes %s." % (binary, do_not)

print x
print y

print "Yo digo: %r." % x
print "Yo tambien digo: '%s'." % y

hilarious = False
joke_evaluation = "Esta broma no es divertida?! %r"

print joke_evaluation % hilarious

w = "Este es el lado izquierdo de..."
e = "un string con un lado derecho."

print w + e
