#Kenny Ruan  TE20D BankUppgift
# Variabler
transactions = []                   # I dennas listan loggas dina transaktioner 
file_name = "transaktioner.txt"      # i denna txt filen loggas dina transaktioner


# Räknar ut ditt saldo
def saldo():
    saldo = 0 
    for t in transactions:
        saldo += t
    return saldo


# loggar alla dina transaktioner
def print_transactions():   
    line = 0
    summa = 0
    output = ("\n   Transaktioner   "
              "\n{:>3} {:>12} {:>12}"
              "\n---------------------").format("Nummer", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    
    return output

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

# checkar ifall det finns en fil, så att den inte skapar en till
def check_file_exists():
    try:
        with open(file_name, "x"):
            print("Filen har skapats")

        with open(file_name, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

# öppnar och läser filen
def read_file():
    check_file_exists()

    with open(file_name) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
            
# loggar dina transaktioner
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

# skickar dina transaktioner till txt filen
def write_transaction_to_file(transaction):
    with open(file_name, "a") as f:
        f.write("{}\n".format(transaction))

read_file()
while True:     
#Jerusalem BANK MENY
    meny = (f"\n-----------------------------------------------------\n"
            "\n           |JERUSALEM BANK|"
            "\n\n--------------------------------------------------"
            "\n\n1. Visa Saldo            :"
            "\n2. Insättning                 :"
            "\n3. Uttag                      :"
            "\n0. Avsluta eller Stoppa programmet  :"
            "\n\n-----------------------------------"
            "\n Gör ditt val:                 \n\n""").format(saldo())


    välj = validate_int(meny, "ERROR")

    if välj == 0:               # avslutar eller stoppar programmet
        break

    elif välj == 1:             # visar dina transaktioner
        print(print_transactions())

    elif välj == 2:             # här sätter man in pengar
        print("     Insättning     ")
        insättning = int(input("    Ange Belopp:    "))
        if insättning > 0:
            add_transaction(insättning, True)
        else:
            print("  ERROR! Instättning måste var mer än 0 ")

    elif välj == 3:             # här tar du ut pengar
        print("       Uttag        ")
        uttag = int(input("    Ange Belopp:    "))
        if uttag <= saldo() and uttag >= 0:
            add_transaction(-uttag, True)
        elif uttag < 0:
            print("Uttaget måste vara mer än 0! ")
        else:
            print(" ERROR! Beloppet kan inte vara mer än ditt SALDO ")


    else:
        print("  ERROR! okänt val!  ")

print("\n Tack och adjö!")