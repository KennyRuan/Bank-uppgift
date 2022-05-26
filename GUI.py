#Kenny Ruan TE20D
from tkinter import *

#variabler
transactions = []                   # Här loggas dina transaktioner
file_name = "transaktioner.txt"      # Filen där transaktionerna loggas

# kollar ditt saldo 
def saldo():
    saldo = 500 
    for t in transactions:
        saldo += t
    print(f"Ditt saldo är: {saldo} kr")

# sätter in pengar 
def insättning():
    print("   Insättning   ")
    insättning = int(input("  Ange Belopp:  \n"))
    if insättning > 0:
            add_transaction(insättning, True)

# loggar alla transaktioner
def print_transactions():   
    line = 0
    summa = 0
    output = ("\n<=>   Transaktioner   <=>"
              "\n{:>3} {:>12} {:>12}"
              "\n --------------------------------").format("nummer", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    
    print(output)

# tar ut pengar
def uttag():
    print("     Uttag     ")
    uttag = int(input("  Ange Belopp:  \n"))
    if uttag <= 500:
        add_transaction(-uttag, True)

# Sänger av bank programmet och rensar transaktionen
def quita():
    window.quit()
    open(file_name, 'w').close()

# Tittar ifall en fil finns, annars skapar den en ny
def check_file_exists():
    try:
        with open(file_name, "x"):
            print("Filen har skapats")

        with open(file_name, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

# Läser vad filen innehåller
def read_file():
    check_file_exists()

    with open(file_name) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
            
# spara transaktioner innuti filen
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

# Skriver ner transaktioner i filen
def write_transaction_to_file(transaction):
    with open(file_name, "a") as f:
        f.write("{}\n".format(transaction))

read_file()

# Detta skapar en window med titel

window = Tk()
window.title("JERUSALEM BANK Ui")
window.configure(bg="seashell2")

# JERUSALEM Bank 

lbl1 = Label(window, text="▶ JERUSALEM Bank ◀", bg="seashell2", fg="sandy brown", font="Helvetica 18 bold")
lbl1.pack()

# Button för att se din saldo

saldobtn = Button(window, text="Saldo", bg="white", width=15, command=saldo)
saldobtn.pack()

# Button för att se transaktion 

transaktioner = Button(window, text="Transaktioner", bg="white", width=15, command=print_transactions)
transaktioner.pack()

# Button för att sätta in pengar

insättningbtn = Button(window, text="Insättning", bg="white", width=15, command=insättning)
insättningbtn.pack()

# Button för att göra uttag

uttagbtn = Button(window, text="Uttag", bg="white", width=15, command=uttag)
uttagbtn.pack()

# Button för att programmet ska avslutas

stopbtn = Button(window, text="Stäng Programmet", bg="white", width=15, command=quita)
stopbtn.pack()

# Fönstrets mainloop
window.mainloop()