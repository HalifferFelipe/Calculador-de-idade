from datetime import date
data = date.today()
print('Hoje é:',data.day,'/',data.month,'/',data.year)

dia = int(input ('Qual o dia do seu aniversario?'))
mes = int(input ('Em que mês? Em numeros'))
ano = input('Em que ano foi seu nascimento?')
idade = int (data.year) - int (ano)
idade1 = int (data.year) - int (ano) - 1
if mes > int (data.month):
   print(dia,'/',mes,'/',ano, 'Parabens você tem então', idade, 'anos!') 
elif dia <= int (data.day):
    print(dia,'/',mes,'/',ano, 'Parabens você tem então', idade, 'anos!')
else:
    print(dia,'/',mes,'/',ano, 'Parabens você tem então', idade1, 'anos!')