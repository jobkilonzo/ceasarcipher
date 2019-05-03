# Caesar Cipher

alphanums = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
enc = input("Do you want to encrypt a message? (Y/N):")
enc = enc.upper()

if enc == "Y":
    toencrypt = input("Please enter A-Z characters to encrypt:")
    toencrypt = toencrypt.upper()
    shift = input("Please enter a number between 1 and 25 to be your cipher key: ")
    shift = int(shift)
    stringenc = ""
    for character in toencrypt:
        pos = alphanums.find(character)
        newp = pos + shift
        if character in alphanums:
            stringenc = stringenc + alphanums[newp]
        else:
            stringenc = stringenc + character

    shift = str(shift)
    print("You used a cipher shift of " + shift)
    print("Your encrypted message reads:")
    print(stringenc.lower())

if enc == "N":
    todecrypt = input("Please enter A-Z characters to dencrypt:")
    todecrypt = todecrypt.upper()
    shift = input("Please enter a number between 1 and 25 to be your cipher key: ")
    shift = int(shift)
    decrypted = ""
    for character in todecrypt:
        pos = alphanums.find(character)
        newp = pos - shift
        if character in alphanums:
            decrypted = decrypted + alphanums[newp]
        else:
            decrypted = decrypted + character

    shift = str(shift)
    print("You used a cipher shift of " + shift)
    print("Your decrypted message reads:")
    print(decrypted)


else:
    print("===== Program End ====== ")
