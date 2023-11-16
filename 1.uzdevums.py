
lietot_skaitlis = int(input("Ievadiet skaitli: "))

if lietot_skaitlis < 1:
    print("Lūdzu, ievadiet pozitīvu skaitli lielāku par 0.")
else:
    summa = 0

    # for cikls
    for skaitlis in range(1, lietot_skaitlis + 1):
        summa += skaitlis

    print(f"Saskaitot no 1 līdz {lietot_skaitlis}, rezultāts ir: {summa}")
