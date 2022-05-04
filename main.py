from cryptography.fernet import Fernet

def writeA(file, adress, nickname, password):
    decryptFile(file)
    f = open(file, "a")
    f.write("\n" + adress + "#" + nickname + "#" + password +  "#0")
    f.close()
    encryptFile(file)

def mPassC(file, adress, nickname, password):
    f = open(file, "a")
    f.write(adress + "#" + nickname + "#" + password + "#0")
    f.close()
    encryptFile(file)

def writeB(file, data):
    f = open(file, "wb")
    f.write(data)
    f.close()

def getDataB(file):
    f = open(file, "rb")
    data = f.read()
    f.close()

    return data

def getDataS(file):
    f = open(file, "r")
    data = f.read()
    f.close()

    return data

def convertToBinary(file):
    f = open(file, "r")
    data = f.read()
    data = bytes(data, 'utf-8')
    f.close()

    return data

def convertToString(file):
    f = open(file, "rb")
    data = f.read()
    data = data.decode("UTF-8")
    f.close()

    return data

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.txt", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encryptFile(file):
    # load the previously generated key
    key = load_key()
    data = convertToBinary(file)

    # initialize the Fernet class
    f = Fernet(key)

    # encrypt the message
    encrypted = f.encrypt(data)
    writeB(file, encrypted)

def decryptFile(file):
    # load the previously generated key
    key = load_key()
    data = getDataB(file)

    # initialize the Fernet class
    f = Fernet(key)

    # encrypt the message
    decrypted = f.decrypt(data)
    writeB(file, decrypted)
    convertToString(file)

def search(file, word):
    with open(file, 'r') as searchfile:
        for line in searchfile:
            if word in line:
                return line

def updatePassword(file, word, updatedWord):
    with open(file, 'r') as fileee:
        filedata = fileee.read()

    filedata = filedata.replace(word, updatedWord)

    with open(file, 'w') as filee:
        filee.write(filedata)

def oneLine(file):
    f = open(file, "r")
    result = f.readline()
    f.close()
    return result

def mainF():

    if(oneLine("password.txt") == ""):
        sifre = input("Ilk sifrenizi olusturun lutfen.")
        mPassC("password.txt", "masterAdminPass" ,sifre ,"testing")

    adminControl = input("Lutfen ana sifrenizi giriniz.")
    decryptFile("password.txt")
    x = search("password.txt", adminControl)
    y = x.split("#")
    encryptFile("password.txt")

    if (y[1] == adminControl):
        print("Basariyla giris yaptiniz.")

        print("1 > yeni bir sifre eklemek istiyorum.")
        print("2 > varolan bir sifreyi sorgulamak istiyorum.")
        print("3 > varolan bir sifreyi guncellemek istiyorum.")
        print("4 > Cikis")

        answer = input()
        if answer == "1":
            adress = input("E mail veya Site adres yada adini yazin.")
            nickname = input("Kullanici adinizi yazin")
            password = input("Sifrenizi yazin.")
            writeA("password.txt", adress, nickname, password)
            print("\nSifreniz Kaydedildi.")

        if answer == "2":
            searchWord = input("Aramak istediginiz site adi veya kullanici adinizi yazin.")
            decryptFile("password.txt")
            line = search("password.txt", searchWord)
            z = line.split("#")
            encryptFile("password.txt")
            print("Sifreniz " + z[2])

        if answer == "3":
            searchWord = input("Degistimek istediginiz site adi veya kullanici adinizi yazin.")
            decryptFile("password.txt")
            line = search("password.txt", searchWord)
            m = line.split("#")
            update = input("Sifreyi ne olarak guncellemek istiyorsunuz?")
            updatePassword("password.txt", m[2], update)
            encryptFile("password.txt")

        if answer == "4":
            return 0
    else:
        print("Sifre yanlis. Uygulama kapaniyor.")


mainF()


