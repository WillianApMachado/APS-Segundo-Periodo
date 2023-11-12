Emissao = {
  "1": ["1- Dioxido de carbono", 0.2727, ],
  "2": ["2- Bromometano", 0.545,],
  "3": ["3- Diclorometano", 2.45],
  "4": ["4- Clorometano", 3.27],
  "5": ["5- Clorofórmio", 4.36],
  "6": ["6- Metano", 7.64],
  "7": ["7- 1,1,1-Tricloroetano", 44],
  "8": ["8- Óxido Nitroso", 72],
  "9": ["9- Tetracloreto de carbono", 472],
  "10": ["10- PerfluoroCiclopropano", 2508],
  "11": ["11- Éter perfluoropolimetilisopropílico", 2647],
  "12": ["12- Triufloreto de nitrogênio", 4390],
  "13": ["13- Pentafluoreto de trifulorometilsulfur", 4744],
  "14": ["14- Hexafluoreto de enxofre", 6408],
}
print ("Escolha o tipo de gás produzido pela sua empresa: ")   
for i in Emissao:
    print (Emissao[i][0])
plista = ""
while plista not in Emissao:
    plista = str(input("Digite um valor correspondente a lista: "))
# ("Aqui se faz o calculo de credito de carbono")
while True:
    qtgas = input("Digite Aqui a quantidade de gases produzidos em toneladas em um mês: " )
    try:
        qtgas = float (qtgas)
        break
    except ValueError:
     print ("Por favor digite um numero")
while True:
    Tempo = input("Digite Aqui quantos meses irá calcular: " )
    try:
        Tempo = float (Tempo)
        break
    except ValueError:
     print ("Por favor digite um numero")
x = (0)
y = (0)
valorfinal = 0
vfinal = (0)
def calculocreditocarbono(x,y,vfinal):
  vfinal = (x * y)
  return vfinal
#Aqui se faz a repetição pro usuario calcular o valor da emissão e credito de carbono de cada produto individual
quebra = ""
while True:
    if quebra == "3":
       break 
    
    
    vfinal = calculocreditocarbono (Emissao[plista][1], qtgas,vfinal)
    valorfinal += vfinal
    print ("Digite a proxima ação a ser feita")
    print ("Ver a lista - '1' ")
    print ("Adicionar gás - '2' ")
    print ("Parar ver o resultado final - '3'")
    quebra = str(input("Digite aqui o comando correspondente: "))
    if quebra == "1":
        for i in Emissao:
          print (Emissao[i][0])
    if quebra == "2":
       plista = ""
       while plista not in Emissao:
          plista = str(input("Digite o valor correspondente a lista: "))
       while True:
        qtgas = input("Digite Aqui a quantidade de gases produzidos em toneladas em um mês: " )
        try:
            qtgas = float (qtgas)
            break
        except ValueError:
         print ("Por favor digite um numero")



valorfinal = valorfinal * Tempo
valorfinaltexto = valorfinal
valorfinaltexto = f'{valorfinaltexto:_.2f}'
valorfinaltexto = valorfinaltexto.replace('.',',').replace('_','.')
print (f"Você produzirá {valorfinaltexto} Tonelada(s) de carbono equivalente em {Tempo:.2f} Mês(es) ") 

creditocarbono = valorfinal
creditocarbonovalor = valorfinal * 25
textocreditocarbonovalor = f'R$ {creditocarbonovalor:_.2f}'
textocreditocarbonovalor = textocreditocarbonovalor.replace('.',',').replace('_','.')
print (f"Você precisará de {valorfinaltexto} Creditos de carbono para alcançar o carbono equivalente produzido, o que irá lhe custar {textocreditocarbonovalor}")

