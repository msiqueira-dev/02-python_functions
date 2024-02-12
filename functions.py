# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python
#   Esse Programa tem como finalidade exibir como funciona funções em Python através do exemplo de conversão de temperaturas
# EN: 
#   This is a comment and will be ignored by Python.
#   This program has the objective of showing how functions work in Python using the temperature conversion as an example

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


print (celsius_to_kelvin(37))
print (celsius_to_fahrenheit(37))
print (celsius_to_kelvin(100))
print (celsius_to_fahrenheit(100))