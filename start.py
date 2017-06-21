import sys

pesel = input("Podaj numer PESEL: ")

print("-----")

if len(pesel) == 11:
    control = 0
    controlVal = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]

    for i in range(0, len(pesel) - 1):
        control += controlVal[i] * int(pesel[i])
    control = control % 10

    if control == int(pesel[10]):
        date = pesel[:6]
        yrsuff = date[:2]
        myr = date[2:4]
        
        if (myr[0] == "8") or (myr[0] == "9"):
            yrpre = "18"
            month = int(myr) - 80
        elif (myr[0] == "0") or (myr[0] == "1"):
            yrpre = "19"
            month = int(myr)
        elif (myr[0] == "2") or (myr[0] == "3"):
            yrpre = "20"
            month = int(myr) - 20
        elif (myr[0] == "4") or (myr[0] == "5"):
            yrpre = "21"
            month = int(myr) - 40
        elif (myr[0] == "6") or (myr[0] == "7"):
            yrpre = "22"
            month = int(myr) - 60

        year = yrpre + yrsuff
        month = str(month)
        day = str(int(date[4:]))
        
        if int(pesel[9]) % 2 == 0:
            gender = "Kobieta"
        elif int(pesel[9]) % 2 != 0:
            gender = "Mezczyzna"

        print("Rok urodzenia: " + year)
        print("Miesiac urodzenia: " + month)
        print("Dzien urodzenia: " + day)
        print("Plec: " + gender)

        sys.exit(0)

    sys.exit("Podano nieprawidlowy numer PESEL!")
print("Podano nieprawidlowy numer PESEL!")