""" 
Brute Force Attack 
Password Cracker For PDF
Download the 'dictionary.txt' file also before tring the program

"""

import PyPDF2 as pd

filename = r"D:\OFFER_LETTER\EAadhaar_605426924835_03102019222815_998941.pdf"

file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not encryted! You can successfully open it!')

else:
    wordListFile = open('dictionary.txt', 'r')
    body = wordListFile.read()#.lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print('Trying dencryption by: {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('Success! The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print('Passwords tried: ' + str(tried))
            continue
