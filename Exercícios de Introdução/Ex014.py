temp = float(input('Qual a temperatura? '))
md = input('Qual a unidade da temperatura? ( Celsius-c, Fahrenheit-f, Kelvin-k ): ')

if md=='c':
    print(f' Fahrennheit = {1.8*temp+32:.2f}° e Kelvin = {temp+273.15:.2f}°')
elif md=='f':
    print(f' Celsius = {(temp-32)/1.8:.2f}° e Kelvin = {(temp-32)*(5/9)+273.15:.2f}°')
elif md=='k':
    print((f' Celsius = {temp-273.15:.2f}° e Fahrenheit = {1.8*(temp-273.15)+32:.2f}'))
else:
    print('Unidade inválida!')