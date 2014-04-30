formatter = "%r %r %r %r"
#Se imprimen los formatter con los valores asignados al frente
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "Tuve esa cosa.",
    "Puede escribir encima.",
    "Pero no cantar.",
    "Entonces Buenas noches."
)
