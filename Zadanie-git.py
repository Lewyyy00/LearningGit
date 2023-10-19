print("Zadanie 1")
#Tworzenie słownika
Lista_zakupow = {
    "piekarnia":["chleb", "bułki", "pączek"],
    "warzywniak":["marchew", "seler", "rukola"]
}
print("Lista zakupów")
#Tworzenie pętli 
for sklep, produkty in Lista_zakupow.items():
    sklep = sklep.capitalize()
    produkty = [produkt.capitalize() for produkt in produkty]
    print(f"idę do {sklep} i kupuje {produkty}")