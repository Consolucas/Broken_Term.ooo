from string import ascii_lowercase as letters
from filter import palavras
from unidecode import unidecode

def resolver(is_in, is_out, **positions):
  
  for palavra in palavras:
    palavra = unidecode(palavra)
    # pra cada letra que tem que estar,
    # se ela não estiver, vai pra próxima
    # palavra
    has_all_in = True
              
    for i in is_in:
      if i not in palavra:
        has_all_in = False
        break

    if not has_all_in: continue

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

resolver(is_in = "", is_out ="crasefibntpjh", e="o", in_b ="ou", in_c="l")
