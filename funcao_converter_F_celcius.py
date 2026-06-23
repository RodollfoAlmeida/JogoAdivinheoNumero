# função que converte fahrenheit para celcius  python funcao_converter_F_celcius.py
# criar função aceitar a temperatura em f
# passar pela formula (f - 32) * 5/9
# retornar o vaor para o escopo global

def f_p_c(f):
    return (f - 32) * 5/9

temp_f = 102
temp_c = f_p_c(temp_f)

print("A temperatura {}F foi covnertida para {}C".format(temp_f, temp_c))