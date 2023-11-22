from collections import Counter
tr=('a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'i', 'i̇', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z')
en = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
class AdditiveChiper:
    """
    !!!! This README.md created wtih AI .So this file is not complete yet. !!!!
    Class representing an Additive Cipher encryption and decryption algorithm.
    """


    def AdditiveChiperEncryp(plaintext,key,alphabet):
        """
        Encrypts the given plaintext using the Additive Cipher algorithm.

        Args:
            plaintext (str): The plaintext to be encrypted.
            key (int): The encryption key.
            alphabet (str): The alphabet used for encryption.

        Returns:
            str: The encrypted ciphertext.
        """
        # If your python verison is 3.10 ,you can use this code .
            # match alphabet:
            #     case ["tr"]:
            #         alphabet=tr
            #     case ["en"]:
            #         alphabet=en
            #     case _:
            #         print("Alphabet not found")
            #         return
        if alphabet == "en" :
            alphabet =en
        elif alphabet =="tr":
                alphabet =tr
        else:
            print("Alphabet not supportted!")
            return 
        chipertext=""
        for charachter in plaintext.lower():
            if charachter in alphabet:
                chipertext+=alphabet[(alphabet.index(charachter)+key)%len(alphabet)]
            else:
                chipertext+="*"
        return chipertext

    def AdditiveChiperDecryp(plaintext,key,alphabet):
        """
        Decrypts the given ciphertext using the Additive Cipher algorithm.

        Args:
            plaintext (str): The ciphertext to be decrypted.
            key (int): The decryption key.
            alphabet (str): The alphabet used for decryption.

        Returns:
            str: The decrypted plaintext.
        """
        # If your python verison is 3.10 ,you can use this code .
            # match alphabet:
            #     case ["tr"]:
            #         alphabet=tr
            #     case ["en"]:
            #         alphabet=en
            #     case _:
            #         print("Alphabet not found")
            #         return
        if alphabet == "en" :
            alphabet =en
        elif alphabet =="tr":
            alphabet =tr
        else:
            print("Alphabet not supportted!")
            return 
        chipertext=""
        for charachter in plaintext.lower():
            if charachter in alphabet:
                chipertext+=alphabet[(alphabet.index(charachter)-key)%len(alphabet)]
            else:
                chipertext+="*"
        return chipertext
    
    def AdditiveChiperCyrptoAnalyze(chipertext):
        """
        !!!It my goal but this module is not complete yet.!!!
        Performs a cryptanalysis on the given ciphertext to determine the encryption key and decrypts it.

        Args:
            chipertext (str): The ciphertext to be analyzed and decrypted.

        Returns:
            str: The decrypted plaintext.
        """
       # Count the frequency of each character in chipertext
        char_counts = Counter(chipertext)
        
        # Find the most frequently occurring character
        most_common_char = char_counts.most_common(1)[0][0]
        
        # Find the key by subtracting the index of the most common character from the index of 'e'
        key = en.index("e") - en.index(most_common_char)
        
        # Decrypt the chipertext by subtracting the key from each character and converting it back to a letter
        plaintext = ""
        for char in chipertext:
            if char in en:
                plaintext += en[(en.index(char) - key) % len(en)]
            else:
                return "Error : I cant find this charachter in alphabet"
        
        return plaintext
# Example usage
"""
    TESTING
"""
plaintext_en="These are short famous texts in English from classic sources like the Bible or Shakespeare Some texts have word definitions and explanations to help you Some of these texts are written in an old style of English Try to understand them because the English that we speak today is based on what our great great great great grandparents spoke before Of course not all these texts were originally written in English The Bible for example is a translation But they are all well known in English today and many of them express beautiful thoughts".replace("\n","").lower()
encrypt_plaintext_en=AdditiveChiper.AdditiveChiperEncryp(plaintext=plaintext_en,key=15,alphabet="en")
  
chipertext = encrypt_plaintext_en
decrypt_plaintext_en=AdditiveChiper.AdditiveChiperDecryp(encrypt_plaintext_en,15,"en").replace("*",",")
if decrypt_plaintext_en == plaintext_en.lower().replace(" ",","):
    print("AdditiveChiper is working")
    print("encrypt_plaintext_en : ",encrypt_plaintext_en)
    print("decrypt_plaintext_en : ",decrypt_plaintext_en)
else:
    print("AdditiveChiper is not working")
    print("plaintext :",plaintext_en.lower().replace(" ",""))
    print("encrypt_plaintext_en : ",encrypt_plaintext_en)
    print("decrypt_plaintext_en : ",decrypt_plaintext_en)


def MultiplicativeChiper(plaintext,key,alphabet):
# If your python verison is 3.10 ,you can use this code .
    # match alphabet:
    #     case ["tr"]:
    #         alphabet=tr
    #     case ["en"]:
    #         alphabet=en
    #     case _:
    #         print("Alphabet not found")
    #         return
    if alphabet == "en" :
        alphabet =en
    elif alphabet =="tr":
        alphabet =tr
    else:
        print("Alphabet not supportted!")
        return 
    chipertext=""
    for charachter in plaintext.lower():
        if charachter in alphabet:
            chipertext+=alphabet[(alphabet.index(charachter)*key)%len(alphabet)]
        else:
            chipertext+="*"
    return chipertext

def AffineChiper(plaintext,key,alphabet):
    if alphabet == "en" :
        alphabet =en
    elif alphabet =="tr":
        alphabet =tr
    else:
        print("Alphabet not supportted!")
        return
    chipertext=""
    for charachter in plaintext.lower():
        if charachter in alphabet:
            chipertext+=alphabet[((alphabet.index(charachter)*key[0])+key[1])%len(alphabet)]
        else:
            chipertext+="*"
    return chipertext

# chipertext_1=AdditiveChiper.AdditiveChiperEncryp(plaintext="hello",key=15,alphabet="tr")
# print(chipertext_1)

# chipertext_2=MultiplicativeChiper("HelLo",7,"en")
# print(chipertext_2)

# chipertext_3=AffineChiper("HelLo",(7,2),"en")
# print(chipertext_3)