from enigma.machine import EnigmaMachine
from itertools import product

#Code sample mainly from https://pypi.org/project/py-enigma/

#Define user interaction stuff:
print("Engima KeyBrute - v0.1 by Insecurities||BeefOverflow")
ciphertext_user = input("[*] Enter cipher text:\n").upper()
crib = input("\n[*] Enter crib: (The longer the crib the better the results)\n").upper()

#Keysheet specs must be known for this to work corrrectly
machine = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings=[1, 20, 11],
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

#Gen list of 3 letter sets. Might not work 100% of time
permkey = product('ABCDEFGHIJKLMNOPQRSTUVWXYZ',repeat=3)
for i in list(permkey):
    #Sets starting pos to possible 3 char
    machine.set_display(i)

# decrypt the message key
    msg_key = machine.process_text(i)

# decrypt the cipher text with the unencrypted message key
    machine.set_display(msg_key)

    ciphertext = ciphertext_user
    plaintext = machine.process_text(ciphertext)

    if crib in plaintext:
        print("[*] MATCH:", plaintext)