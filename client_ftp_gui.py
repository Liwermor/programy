#Klient FTP z gui napisany z pomocą pakietu Tkinter
import tkinter as tk
from tkinter import BOTH, END, LEFT
import ftplib
import os
import sys

ftp = ftplib.FTP()

def Polaczenie():
    ip = pole_adres.get()
    port = int(pole_port.get())
    try:
        odpowiedz = ftp.connect(ip, port)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
        etykieta_login.place(x=20, y=20)
        pole_login.place(x=20, y=40)
        etykieta_haslo.place(x=150, y=20)
        pole_haslo.place(x=150, y=40)
        przycisk_zaloguj.place(x=280, y=40)
        etykieta_adres.place_forget()
        pole_adres.place_forget()
        etykieta_port.place_forget()
        pole_port.place_forget()
        przycisk_polacz.place_forget()
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Nie da sie połączyć!")


def zaloguj():
    user = pole_login.get()
    password = pole_haslo.get()
    try:
        odpowiedz = ftp.login(user, password)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
        wyswietl_katalog()
        etykieta_login.place_forget()
        pole_login.place_forget()
        etykieta_haslo.place_forget()
        pole_haslo.place_forget()
        przycisk_zaloguj.place_forget()

    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Nie udało się zalogować!")


def wyswietl_katalog():
    lista_plikow = list(ftp.nlst())
    a = 0
    okno_lista_plikow.delete(0, END)
    for item in lista_plikow:
        okno_lista_plikow.insert("end", str(a) + ". " + item)
        a += 1



def zmien_katalog():
    katalog = pole_wejscie.get()
    try:
        odpowiedz = ftp.cwd(katalog)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Zmiana katalogu niemożliwa!")
    wyswietl_katalog()


def stworz_katalog():
    katalog = pole_wejscie.get()
    try:
        odpowiedz = ftp.mkd(katalog)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Utworzenie katalogu niemożliwe!")
    wyswietl_katalog()


def usun_katalog():
    katalog = pole_wejscie.get()
    try:
        odpowiedz = ftp.rmd(katalog)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Usunięcie katalogu niemożliwe!")
    wyswietl_katalog()


def usun_plik():
    plik = pole_wejscie.get()
    try:
        odpowiedz = ftp.delete(plik)
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, odpowiedz)
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Usunięcie plikue niemożliwe!")
    wyswietl_katalog()


def pobierz_plik():
    file = pole_wejscie.get()
    down = open(file, "wb")
    try:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Pobieranie pliku: " + file + "...")
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, ftp.retrbinary("RETR " + file, down.write))
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Błąd pobierania pliku")
    wyswietl_katalog()


def dodaj_plik():
    file = pole_wejscie.get()
    try:
        up = open(file, "rb")
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Wysyłanie " + file + "...")
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, ftp.storbinary("STOR " + file, up))
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Błąd wysyłania pliku!")
    wyswietl_katalog()


def zakoncz_polaczenie():
    try:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Rozłączam...")
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, ftp.quit())
        sys.exit("Koniec sesji")
    except:
        odpowiedz_serwera.insert(END, "\n")
        odpowiedz_serwera.insert(END, "Błąd połączenia!")


def wyslij_katalog():
    print("kutaz")
    sndcmd = "mput ."
    ftp.sendcmd(sndcmd)


def downloadFiles(path, destination):
    # path & destination are str of the form "/dir/folder/something/"
    # path should be the abs path to the root FOLDER of the file tree to download
    try:
        ftp.cwd(path)
        # clone path to destination
        os.chdir(destination)
        os.mkdir(destination[0:len(destination) - 1] + path)
        print(destination[0:len(destination) - 1] + path + " built")
    except OSError:
        # folder already exists at destination
        pass
    except ftplib.error_perm:
        # invalid entry (ensure input form: "/dir/folder/something/")
        print("error: could not change to " + path)
        sys.exit("ending session")

    # list children:
    filelist = ftp.nlst()

    for file in filelist:
        try:
            # this will check if file is folder:
            ftp.cwd(path + file + "/")
            # if so, explore it:
            downloadFiles(path + file + "/", destination)
        except ftplib.error_perm:
            # not a folder with accessible content
            # download & return
            os.chdir(destination[0:len(destination) - 1] + path)
            # possibly need a permission exception catch:
            with open(os.path.join(destination, file), "wb") as f:
                ftp.retrbinary("RETR " + file, f.write)
            print(file + " download")
def pobierz_katalog():
    path = pole_wejscie.get()
    destination = "C:/Users/Public/"
    downloadFiles(path, destination)

okno = tk.Tk()
okno.title("Klient FTP")
#okno.wm_iconbitmap("favicon.ico")
okno.geometry("1000x600")


etykieta_adres = tk.Label(okno, text="Adres serwera")
pole_adres = tk.Entry(okno)
etykieta_port = tk.Label(okno, text="Port")
pole_port = tk.Entry(okno)
przycisk_polacz = tk.Button(okno, text="Połącz",height = 1, width = 5, command=Polaczenie)


odpowiedz_serwera = tk.Text(okno)


etykieta_login = tk.Label(okno, text="Użytkownik")
pole_login = tk.Entry(okno)
etykieta_haslo = tk.Label(okno, text="Hasło")
pole_haslo = tk.Entry(okno)
przycisk_zaloguj = tk.Button(okno, text="Zaloguj", command=zaloguj)


etykieta_katalog = tk.Label(okno, text="Zawartośc katalogu:")
okno_lista_plikow = tk.Listbox(okno, width=45, height=14)


etykieta_wejscie = tk.Label(okno, text="Wprowadź nazwę katalogu/pliku")
pole_wejscie = tk.Entry(okno)
przycisk_zmien_katalog = tk.Button(okno, text="Zmień katalog", command=zmien_katalog, width=15)
przycisk_stworz_katalog = tk.Button(okno, text="Stwórz katalog", command=stworz_katalog, width=15)
przycisk_usun_katalog = tk.Button(okno, text="Usuń katalog", command=usun_katalog, width=15)
przycisk_usun_plik = tk.Button(okno, text="Usuń plik", command=usun_plik, width=15)
przycisk_pobierz_plik = tk.Button(okno, text="Pobierz plik", command=pobierz_plik, width=15)
przycisk_wyslij_plik = tk.Button(okno, text="Wyślij plik", command=dodaj_plik, width=15)
przycisk_rozlacz = tk.Button(okno, text="Rozłącz", command=zakoncz_polaczenie, width=15)
przycisk_pob_katalog = tk.Button(okno, text="pobierz katalog", command=pobierz_katalog(), width=15)
przycisk_wys_katalog = tk.Button(okno, text="Wyslij katalog", command=wyslij_katalog, width=15)


etykieta_adres.place(x=20, y=20)
pole_adres.place(x=20, y=40)
etykieta_port.place(x=150, y=20)
pole_port.place(x=150, y=40)
przycisk_polacz.place(x=280, y=40)
odpowiedz_serwera.place(x=20, y=150)

etykieta_katalog.place(x=700, y=295)
okno_lista_plikow.place(x=700, y=312)

etykieta_wejscie.place(x=750, y=200)
pole_wejscie.place(x=770, y=220)
przycisk_zmien_katalog.place(x=20, y=70)
przycisk_stworz_katalog.place(x=150, y=70)
przycisk_usun_katalog.place(x=280, y=70)
przycisk_usun_plik.place(x=410, y=70)
przycisk_pob_katalog.place(x=20, y=110)
przycisk_wys_katalog.place(x=150, y=110)

przycisk_pobierz_plik.place(x=540, y=70)
przycisk_wyslij_plik.place(x=670, y=70)
przycisk_rozlacz.place(x=800, y=70)


okno.mainloop()
