lietotaja_cipars = int(input("Ievadiet skaitli: "))

if lietotaja_cipars < 0:
    print("Faktoriāls nav definēts negatīviem skaitļiem.")
elif lietotaja_cipars == 0:
    print("Faktoriāls no 0 ir 1.")
else:
    faktorials = 1

    for skaitlis in range(1, lietotaja_cipars + 1):
        faktorials *= skaitlis

print(f"Faktoriāls no {lietotaja_cipars} ir: {faktorials}")
