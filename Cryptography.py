from collections import Counter
tr=('a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'i', 'i̇', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z')
en = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
def modInverse(A, M): 
            m0 = M 
            y = 0
            x = 1
        
            if (M == 1): 
                return 0

            while (A > 1): 
        
                # q is quotient 
                q = A // M 
        
                t = M 
        
                # m is remainder now, process 
                # same as Euclid's algo 
                M = A % M 
                A = t 
                t = y 
        
                # Update x and y 
                y = x - q * y 
                x = t 
        
            # Make x positive 
            if (x < 0): 
                x = x + m0 
        
            return x 
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
class MultiplicativeChiper:
        def MultiplicativeChiperEncryp(plaintext,key,alphabet):
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

        def MultiplicativeChiperDecryp(plaintext,key,alphabet):
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
            if alphabet == "en":
                alphabet = en
            elif alphabet == "tr":
                alphabet = tr
            else:
                print("Alphabet not supported!")
                return

            key = modInverse(key, len(alphabet))
            if key == -1:
                print("Key not found")
                return

            chipertext = ""
            for charachter in plaintext.lower():
                if charachter in alphabet:
                    chipertext += alphabet[(alphabet.index(charachter) * key) % len(alphabet)]
                else:
                    chipertext += "*"
            return chipertext
class AffineChiper:
    def AffineChiperEncryp(plaintext,key,alphabet):
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
    def AffineChiperDecryp(chipertext,key,alphabet):
        if alphabet == "en" :
            alphabet =en
        elif alphabet =="tr":
            alphabet =tr
        else:
            print("Alphabet not supportted!")
            return
        key =modInverse(key[0],len(alphabet)),key[1]
        plaintext=""
        for charachter in chipertext.lower():
            if charachter in alphabet:
                plaintext+=alphabet[((alphabet.index(charachter)-key[1])*key[0])%len(alphabet)]
            else:
                plaintext+="*"
        return plaintext