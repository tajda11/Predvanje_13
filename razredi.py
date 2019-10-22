import json

class Oseba:
    ime = None
    priimek = None
    email = None

    def polno_ime(self):
        return self.ime + " " + self.priimek

class Uporabnik (Oseba):
    #ime = None
    #priimek = None
    #email = None
    je_blokiran = False

    #def polno_ime(self):
        #return self.ime + " " + self.priimek

    def shrani(self):
        ime_datoteke = self.ime + "-" + self.priimek + ".txt"
        with open(ime_datoteke, "w") as datoteka:
            podatki = self.__dict__
            datoteka.write(json.dumps(podatki))

class Moderator(Oseba):
    #ime = None
    #priimek = None
    #email = None
    pravice = []

    #def polno_ime(self):
        #return self.ime + " " + self.priimek

    def ima_pravico(self, pravica):
        return pravica in self.pravice


uporabnik1 = Uporabnik()
uporabnik1.ime = "Miha"
uporabnik1.priimek = "Novak"
uporabnik1.email = "miha.novak@email.si"
#uporabnik1.je_blokiran = False

uporabnik2 = Uporabnik()
uporabnik2.ime = "Ana"
uporabnik2.priimek = "Kos"
uporabnik2.email = "ana.kos@email.com"
uporabnik2.je_blokiran = True

print(uporabnik1.polno_ime())
print(uporabnik2.polno_ime())
uporabnik1.shrani()
uporabnik2.shrani()

mod1.email = "a "