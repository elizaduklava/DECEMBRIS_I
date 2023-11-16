import datetime

tagad = datetime.datetime.now().hour

if 4 <= tagad < 12:
    sveic = "Labrīt!"
elif 12 <= tagad < 17:
    sveic = "Labdien!"
else:
    sveic = "Labvakar!"

print(sveic)
