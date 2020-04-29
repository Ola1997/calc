#kalkulator
print("Wpisz pierwszą liczbę")
pierwsza_liczba = float(input())

print("Działanie matematyczne")
działanie = input()

print("Wpisz drugą liczbę")
druga_liczba = float(input())


while działanie == "+":
  wynik = pierwsza_liczba + druga_liczba

elif działanie == "-":
  wynik = pierwsza_liczba - druga_liczba

elif działanie == "*":
  wynik = pierwsza_liczba * druga_liczba 

elif działanie == "/":
  wynik = pierwsza_liczba / druga_liczba

else:
  print("Niewłasciwy zapis")

print(wynik)

print("Twój wynik to: " + wynik)


