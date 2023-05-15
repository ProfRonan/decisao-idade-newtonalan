id = int(input(" "))

if id < 0:
  print("Impossível!")
elif 0 < id < 18:
  print("Não precisa se alistar.")
elif 18 < id < 65:
  print("Não esqueça de votar na próxima eleição.")
elif id > 65:
  print("Vá descansar.")
else:
  print("Eita!")
