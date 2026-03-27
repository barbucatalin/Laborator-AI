import datetime


def extrage_componente_data():
 
    acum = datetime.datetime.now()


    an = lambda d: d.year
    luna = lambda d: d.month
    zi = lambda d: d.day
    ora_completa = lambda d: d.strftime("%H:%M:%S.%f")

    print(f"Data completă: {acum}")
    print(f"Anul:          {an(acum)}")
    print(f"Luna:          {luna(acum):02d}")
    print(f"Ziua:          {zi(acum):02d}")
    print(f"Ora:           {ora_completa(acum)}")


if __name__ == "__main__":
    extrage_componente_data()