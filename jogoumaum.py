
mao1a = 1
mao2a = 1
mao1b = 1
mao2b = 1

def cena(): 
  print("Jogador a:")
  print(f"mão 1: {mao1a} dedos e mão 2: {mao2a} dedos")
  print("Jogador b:")
  print(f"mão 1: {mao1b} dedos e mão 2: {mao2b} dedos ")

def menu():
  escolha = 0
  while escolha != 1 and escolha != 2:
      escolha= int(input("Caso deseje ver as regras digite 1, caso queira jogar digite 2: "))
      if escolha == 1:
       print()
       print("Cada jogador tem duas mãos, e no começo cada uma delas possuem um dedo, o jogador pode escolher usar uma de suas mãos para atacar uma mão do outro. ")
       print("Se você tiver 2 dedos e atacar uma mão com 2 dedos, haverá uma soma e a mão atacada terá agora 4 dedos. Caso uma mão seja atacada e fique com o total de 5 dedos você perde ela")
       print("caso passe de 5 o valor será diminuido por 5. O objetivo é fazer o adversário perder as 2 mãos")
       print("você também pode dividir uma mão, por exemplo, caso você tenha 4 dedos em uma mão você pode transferir seus dedos para uma outra.")
       menu()
      elif escolha == 2:
       gameplay()

def gameplay():

    global jogoativo
    global jogada
    global mao1a
    global mao1b
    global mao2a
    global mao2b

    cena()

    while jogoativo == True:  

        jogadaconcluida = False 
        print("Rodada: ",jogada +1, " | ", "Jogador ", jogada %2 +1, '\n')
        
        print()

        atacar = int(input("Selecione sua mão: "))
        alvo = int(input("selecione qual mão irá atacar, caso queira fazer uma divisão digite 3: "))
        print()    
        if atacar == 1 and alvo == 1:
           mao1b = mao1b + mao1a
           jogadaconcluida == True

        elif atacar == 1 and alvo ==2:
           mao2b = mao2b + mao1a 
           jogadaconcluida == True

        elif atacar == 2 and alvo == 1:
           mao1b = mao1b + mao2a  
           jogadaconcluida == True

        elif atacar == 2 and alvo == 2:
           mao2b = mao2b + mao2a  
           jogadaconcluida == True

        elif atacar == 1 and alvo == 3: 
           valor_troca1 = int(input("Digite quantos dedos você quer passar: "))
           mao2a = mao2a + valor_troca1
           mao1a = mao1a - valor_troca1  
           jogadaconcluida == True

        elif atacar == 2 and alvo == 3: 
           valor_troca2 = int(input("Digite quantos dedos você quer passar: "))
           mao1a = mao1a + valor_troca2
           mao2a = mao2a - valor_troca2
           jogadaconcluida == True

        else: 
         print("jogada invalida")
         gameplay()

        mao1b = mao1b % 5    
        mao2b = mao2b % 5    
        mao1a = mao1a % 5    
        mao2a = mao2a % 5
        
        jogada = jogada + 1

        cena()

        print("Rodada: ",jogada +1, " | ", "Jogador ", jogada %2 +1, '\n')

        atacar = int(input("Selecione sua mão: "))
        alvo = int(input("selecione qual mão irá atacar, caso queira fazer uma divisão digite 3: "))
        print()    
        if atacar == 1 and alvo == 1:
           mao1a = mao1a + mao1b
           jogadaconcluida == True

        elif atacar == 1 and alvo ==2:
           mao2a = mao2a + mao1b
           jogadaconcluida == True

        elif atacar == 2 and alvo == 1:
           mao1a = mao1a + mao2b
           jogadaconcluida == True

        elif atacar == 2 and alvo == 2:
           mao2a = mao2a + mao2b
           jogadaconcluida == True

        elif atacar == 1 and alvo == 3: 
           valor_troca1 = int(input("Digite quantos dedos você quer passar: "))
           mao2b = mao2b + valor_troca1
           mao1b = mao1b - valor_troca1  
           jogadaconcluida == True

        elif atacar == 2 and alvo == 3: 
           valor_troca2 = int(input("Digite quantos dedos você quer passar: "))
           mao1b = mao1b + valor_troca2
           mao2b = mao2b - valor_troca2
           jogadaconcluida == True
           break
        else: 
            print("jogada invalida")

        
        mao1b = mao1b % 5    
        mao2b = mao2b % 5    
        mao1a = mao1a % 5    
        mao2a = mao2a % 5

        
        cena()
        if mao1a == 0 and mao2a == 0:
            printvitoria()
            jogoativo = False 
        if mao1b == 0 and mao2b == 0:
            printvitoria()
            jogoativo = False

        jogada = jogada + 1

def printvitoria():
      global jogada

      print('Jogador',jogada%2 +1 ,'ganhou após', jogada+1, 'rodadas!' )
      print()
      cena()

jogoativo = True
jogada = 0

menu()