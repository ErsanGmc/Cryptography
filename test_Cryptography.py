# Description: This file contains the test cases for the Cryptography module.
from Cryptography import AdditiveChiper , MultiplicativeChiper,AffineChiper
def test_AdditiveCipher():
    plaintext = "hello"
    key = 3
    alphabet = "en"
    expected_ciphertext = "khoor"
    expected_decrypted_text = "hello"
    
    ciphertext = AdditiveChiper.AdditiveChiperEncryp(plaintext, key, alphabet)
    decrypted_text = AdditiveChiper.AdditiveChiperDecryp(ciphertext, key, alphabet)
    
    assert ciphertext == expected_ciphertext, f"Test case 1 failed: Expected ciphertext {expected_ciphertext}, but got {ciphertext}"
    assert decrypted_text == expected_decrypted_text, f"Test case 1 failed: Expected decrypted text {expected_decrypted_text}, but got {decrypted_text}"
    
    plaintext = "merhaba"
    key = 5
    alphabet = "tr"
    expected_ciphertext = "riülefe"
    expected_decrypted_text = "merhaba"
    
    ciphertext = AdditiveChiper.AdditiveChiperEncryp(plaintext, key, alphabet)
    decrypted_text = AdditiveChiper.AdditiveChiperDecryp(ciphertext, key, alphabet)
    
    assert ciphertext == expected_ciphertext, f"Test case 2 failed: Expected ciphertext {expected_ciphertext}, but got {ciphertext}"
    assert decrypted_text == expected_decrypted_text, f"Test case 2 failed: Expected decrypted text {expected_decrypted_text}, but got {decrypted_text}"
    print("Test case 0 :AdditiveChiper  passed!")

    # # Test case 3: Cryptanalysis on a ciphertext
    # ciphertext = "khoor"
    # expected_decrypted_text = "hello"
    
    # decrypted_text = AdditiveChiper.AdditiveChiperCyrptoAnalyze(ciphertext)
    
    # assert decrypted_text == expected_decrypted_text, f"Test case 3 failed: Expected decrypted text {expected_decrypted_text}, but got {decrypted_text}"

def test_MultiplicativeChiperEncryp():
    plaintext = "hello"
    key = 7
    alphabet = "en"
    expected_output = "xczzu"
    assert MultiplicativeChiper.MultiplicativeChiperEncryp(plaintext, key, alphabet) == expected_output

    plaintext = "world"
    key = 5
    alphabet = "en"
    expected_output = "gshdp"
    assert MultiplicativeChiper.MultiplicativeChiperEncryp(plaintext, key, alphabet) == expected_output

    plaintext = "merhaba"
    key = 7
    alphabet = "tr"
    expected_output = "öfueaga"
    assert MultiplicativeChiper.MultiplicativeChiperEncryp(plaintext, key, alphabet) == expected_output
    print("Test case 1 :MultiplicativeChiperEncryp  passed!")


def test_MultiplicativeChiperDecryp():
    ciphertext = "xczzu"
    key = 7
    alphabet = "en"
    expected_output = "hello"
    assert MultiplicativeChiper.MultiplicativeChiperDecryp(ciphertext, key, alphabet) == expected_output

    ciphertext = "gshdp"
    key = 5
    alphabet = "en"
    expected_output = "world"
    assert MultiplicativeChiper.MultiplicativeChiperDecryp(ciphertext, key, alphabet) == expected_output

    ciphertext = "öfueaga"
    key = 7
    alphabet = "tr"
    expected_output = "merhaba"
    assert MultiplicativeChiper.MultiplicativeChiperDecryp(ciphertext, key, alphabet) == expected_output
    print("Test case 2 :MultiplicativeChiperDecryp  passed!")

def test_AffineChiper():
    plaintext = "hello"
    key=[7,2]
    alphabet = "en"
    expected_output = "zebbw"
    assert AffineChiper.AffineChiperEncryp(plaintext, key, alphabet) == expected_output
    assert AffineChiper.AffineChiperDecryp(expected_output, key, alphabet) == plaintext
    print("Test case 3 :Affine Chiper  passed!")
    

test_AdditiveCipher()
test_MultiplicativeChiperEncryp()
test_MultiplicativeChiperDecryp()
test_AffineChiper()
print("All tests passed!")