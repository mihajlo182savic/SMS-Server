from utils import Database

DB = Database('databases/sms.db')

DB.execute("""
    CREATE TABLE Adresa (
        AdresaID INTEGER PRIMARY KEY,
        Adresa TEXT, Grad TEXT, Drzava TEXT
    ); """)

DB.execute("""
    CREATE TABLE Osoba (
        OsobaID INTEGER PRIMARY KEY,
        Ime TEXT, Prezime TEXT,
        AdresaID INTEGER,
        FOREIGN KEY(AdresaID) REFERENCES Adresa(AdresaID)
    ); """)

DB.execute("""
    CREATE TABLE Kontakt (
        KontaktID INTEGER PRIMARY KEY,
        Broj TEXT, Email TEXT,
        OsobaID INTEGER,
        FOREIGN KEY(OsobaID) REFERENCES Osoba(OsobaID)
    ); """)

DB.execute("""
    CREATE TABLE Status (
        StatusID INTEGER PRIMARY KEY,
        Status TEXT, Podstatus TEXT
    ); """)

DB.execute("""
    CREATE TABLE Korisnik (
        KorisnikID INTEGER PRIMARY KEY,
        KorisnickoIme TEXT, Lozinka TEXT,
        OsobaID INTEGER, StatusID INTEGER,
        FOREIGN KEY(OsobaID) REFERENCES Osoba(OsobaID),
        FOREIGN KEY(StatusID) REFERENCES Status(StatusID)
    ); """)
#https://dbdesigner.net/designer/schema/new
