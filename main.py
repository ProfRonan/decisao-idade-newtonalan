n = (input("Digite um numero:\n"))
print(" ")


if n.isnumeric():
  n = int(n)
  if n < 0:
    print("Impossivel!")
  elif n < 18:
    print("O alistamento não é necessário.")
  elif 18 <= n <= 65:
    print("Não deixe de votar na próxima eleição.")
  elif n > 65:
    print("Vá descansar.")

else:
  print("Eita.")
