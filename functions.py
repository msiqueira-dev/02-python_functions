# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python
#   Esse Programa tem como finalidade exibir como funciona funções em Python através do exemplo de conversão de temperaturas
# EN: 
#   This is a comment and will be ignored by Python.
#   This program has the objective of showing how functions work in Python using the temperature conversion as an example

def celsius_to_kelvin(celsius):
    """ 
        PT-BR:
            Isso é um comentário padrão de funções e será ignorado pelo Python
            Essa função recebe um valor por parametro em celsius, aplica o calculo de conversão e
            armazena o resultado em uma variavel kelvin, retorna o valor de kelvin
        EN: 
            This is a function comment and will be ignored by Python.
            This function receives a value in the parameter celsius, it them applies the conversion math and
            stores the result in the variable kelvin, returning it
    """
    kelvin = celsius + 273
    return kelvin

def celsius_to_fahrenheit(celsius):
    """ 
        PT-BR:
            Isso é um comentário padrão de funções e será ignorado pelo Python
            Essa função recebe um valor por parametro em celsius, aplica o calculo de conversão e
            armazena o resultado em uma variavel fahrenheit, retorna o valor de fahrenheit
        EN: 
            This is a function comment and will be ignored by Python.
            This function receives a value in the parameter celsius, it them applies the conversion math and
            stores the result in the variable fahrenheit, returning it
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


print (celsius_to_kelvin(37))
print (celsius_to_fahrenheit(37))
print (celsius_to_kelvin(100))
print (celsius_to_fahrenheit(100))