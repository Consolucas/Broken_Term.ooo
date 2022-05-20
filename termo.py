from string import ascii_lowercase as letters
from filter import palavras
from unidecode import unidecode

def resolver(is_out, **positions):
  
  for palavra in palavras:
    palavra = unidecode(palavra)

    # pra cada letra que não tem que estar,
    # se ela estiver, vai pra próxima palavra
    has_not_in = True

    for i in is_out:
      if i in palavra:
        has_not_in = False
        break

    if not has_not_in: continue

    # pra cada letra (representa posição), 
    # verifica se o usuário especificou que
    # letra está nessa posição, se sim, verifica
    # se ela está mesmo, se não estiver, vai pra
    # próxima palavra
    has_correct_pos = True

    for i in range(5):
      pos = "abcde"[i]
      if pos in positions:
        letter = positions[pos]
        if palavra[i] != letter:
          has_correct_pos = False
          break

    if not has_correct_pos: continue



    # para cada letra que está presente na palavra,
    # mas não está na posição correta
    has_incorrect_pos = True

    for i in range(5):
      in_pos = ["in_a", "in_b", "in_c", "in_d", "in_e"][i]
      if in_pos in positions:
        for in_letter in positions[in_pos]:
          if palavra[i] == in_letter or in_letter not in palavra:
            has_incorrect_pos = False
            break

    if not has_incorrect_pos: continue



    print(palavra)

# para cada letra em cinza, escreva-a em is_out
# para cada letra em amarelo, digite-a em in_"letra da posição"= "letra" ---- ex: in_a = "c"
# para cada letra em verde, digite-a em "letra da posição"= "letra" ---- ex: a = "d"
# posição 1 = a, posição 2 = b ...

resolver(is_out ="")
