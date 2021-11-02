from secrets import token_bytes
import sys

class Encrypt:
    def secretKey(self,length):
        tb:bytes =token_bytes(length)
        return int.from_bytes(tb,"big")

    def encrypt(self,originalData):
        originalByte: bytes = originalData.encode()

        SecreteKeyData:int =self.secretKey(len(originalByte)) #10
        # print("Secret Key importanat:",SecreteKeyData)

        plaintTextData:int =int.from_bytes(originalByte,"big")
        # print("Data of Plain Text",plaintTextData)

        ciphterText:int = plaintTextData ^  SecreteKeyData
        # print("Ciphter Text",ciphterText)
        return ciphterText , SecreteKeyData

    def decrypt(self,ciphterText,SecretkeyData):
        decrpted:int = ciphterText ^ SecretkeyData
        print("Decrypted Data",decrpted)
        bytes_Data =decrpted.to_bytes((decrpted.bit_length()+7)//8, "big")
        return bytes_Data.decode()


# if __name__ =="__main__":
#     originalData = "Encryption With Xor"
#     objEncrypt = Encrypt()
#     ciphterText,SecretkeyData = objEncrypt.encrypt(originalData)
#
#     FinalResult= objEncrypt.decrypt(ciphterText,SecretkeyData)
#     # print("Final Decrypted Result",FinalResult)
