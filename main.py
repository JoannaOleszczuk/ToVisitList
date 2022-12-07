PlacesToVisit = []
Cost = ""
Date = ""
PersonAmount = 0
KeyboardInput = ""

while True:
    KeyboardInput = input("Do jakiego miasta jedziesz? (wpisz koniec, gdy chcesz zakończyć działanie programu) ")
    if KeyboardInput == "koniec":
        break
    Cost = input("Ile kosztuje pobyt za osobę? ")
    Date = input("Podaj miesiąc wyjazdu:")
    PersonAmount = input("Podaj liczbę osób: ")
    ListElement = [KeyboardInput, Cost, Date, PersonAmount]
    PlacesToVisit.append(ListElement)

# print("Miasta do których chcę pojechać to ", end="")
# for Cities in PlacesToVisit:
#     print(str(Cities), end=", ")

FinalResult = "Miasta do których chce pojechać to: "
Sum = 0
PlacesToVisit.sort()

for Cities in PlacesToVisit:
    FinalResult = FinalResult + Cities[0] + " (" + Cities[2] +  ", liczba osób wynosi: " + Cities[3] + ") "
    Sum = Sum + (int(Cities[1])* int(Cities[3]))
FinalResult = FinalResult.removesuffix(",")
FinalResult = FinalResult + " a sumaryczny koszt pobytu za wszystkie osoby wynosi " + str(Sum) + "."
print(FinalResult)

# Vacation = ["Wawa", 100]
# Vacation2 = ["Florencja", 5000]
# Vacation3 = [Vacation, Vacation2]
# print(Vacation)
# print(Vacation2)
# print(Vacation3)






