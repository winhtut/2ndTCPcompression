class Compressed:
    def __init__(self,gene: str,received: int):
        self.received :int = received
        self._compress(gene)

    def _compress(self,gene: str):
        self.bit_string: int = 1 # start with initial value
        for nucleotide in gene.upper():
            binData = bin(self.bit_string)
            self.bit_string <<=5 #shift left two bits
            binData2 = bin(self.bit_string)

            if nucleotide == "A":
                self.bit_string |= 0b00000
                print("A Data :",bin(self.bit_string))

            elif nucleotide == "B":
                self.bit_string |= 0b00001
                print("B Data:",bin(self.bit_string))

            elif nucleotide == "C":
                self.bit_string |= 0b00010
                print("C Data:",bin(self.bit_string))

            elif nucleotide == "D":
                self.bit_string |= 0b00011
                print("D Data:",bin(self.bit_string))

            elif nucleotide == "E":
                self.bit_string |= 0b00100
                print("E Data :",bin(self.bit_string))

            elif nucleotide == "F":
                self.bit_string |= 0b00101
                print("F Data:",bin(self.bit_string))

            elif nucleotide == "G":
                self.bit_string |= 0b00110
                print("G Data:",bin(self.bit_string))

            elif nucleotide == "H":
                self.bit_string |= 0b00111
                print("H Data:",bin(self.bit_string))

            elif nucleotide == "I":
                self.bit_string |= 0b01000
                print("I Data :",bin(self.bit_string))

            elif nucleotide == "J":
                self.bit_string |= 0b01001
                print("J Data:",bin(self.bit_string))

            elif nucleotide == "K":
                self.bit_string |= 0b01010
                print("K Data:",bin(self.bit_string))

            elif nucleotide == "L":
                self.bit_string |= 0b01011
                print("L Data:",bin(self.bit_string))


            elif nucleotide == "M":
                self.bit_string |= 0b01100
                print("M Data :",bin(self.bit_string))

            elif nucleotide == "N":
                self.bit_string |= 0b01101
                print("N Data:",bin(self.bit_string))

            elif nucleotide == "O":
                self.bit_string |= 0b01110
                print("O Data:",bin(self.bit_string))

            elif nucleotide == "P":
                self.bit_string |= 0b01111
                print("P Data:",bin(self.bit_string))

            elif nucleotide == "Q":
                self.bit_string |= 0b10000
                print("Q Data :",bin(self.bit_string))

            elif nucleotide == "R":
                self.bit_string |= 0b10001
                print("R Data:",bin(self.bit_string))

            elif nucleotide == "S":
                self.bit_string |= 0b10010
                print("S Data:",bin(self.bit_string))

            elif nucleotide == "T":
                self.bit_string |= 0b10011
                print("T Data:",bin(self.bit_string))


            elif nucleotide == "U":
                self.bit_string |= 0b10100
                print("U Data :",bin(self.bit_string))

            elif nucleotide == "V":
                self.bit_string |= 0b10101
                print("V Data:",bin(self.bit_string))

            elif nucleotide == "W":
                self.bit_string |= 0b10110
                print("W Data:",bin(self.bit_string))

            elif nucleotide == "X":
                self.bit_string |= 0b10111
                print("X Data:",bin(self.bit_string))

            elif nucleotide == "Y":
                self.bit_string |= 0b11000
                print("Y Data:",bin(self.bit_string))

            elif nucleotide == "Z":
                self.bit_string |= 0b11001
                print("Z Data:",bin(self.bit_string))

            else:
                raise ValueError("Invalid Nucleotide:{0}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""


        for i in range(0, self.received.bit_length() - 1, 5):  # -1 to exlude sentinel

            test = self.received >> i
            testBin = bin(test)
            test2 = test & 0b11

            bits: int = self.received >> i & 0b11111

            if bits == 0b00000:
                gene += "A"
            elif bits == 0b00001:
                gene += "B"
            elif bits == 0b000010:
                gene += "C"
            elif bits == 0b00011:
                gene += "D"

            elif bits == 0b00100:
                gene += "E"
            elif bits == 0b00101:
                gene += "F"
            elif bits == 0b00110:
                gene += "G"

            elif bits == 0b00111:
                gene += "H"
            elif bits == 0b01000:
                gene += "I"

            elif bits == 0b01001:
                gene += "J"

            elif bits == 0b01010:
                gene += "K"
            elif bits == 0b01011:
                gene += "L"
            elif bits == 0b01100:
                gene += "M"

            elif bits == 0b01101:
                gene += "N"
            elif bits == 0b01110:
                gene += "O"
            elif bits == 0b01111:
                gene += "P"

            elif bits == 0b10000:
                gene += "Q"
            elif bits == 0b10001:
                gene += "R"
            elif bits == 0b10010:
                gene += "S"

            elif bits == 0b10011:
                gene += "T"
            elif bits == 0b10100:
                gene += "U"
            elif bits == 0b10101:
                gene += "V"

            elif bits == 0b10110:
                gene += "W"
            elif bits == 0b10111:
                gene += "X"
            elif bits == 0b11000:
                gene += "Y"

            elif bits == 0b11001:
                gene += "Z"

            else:
                raise ValueError("Invalid bits:", bits)

        return gene[::-1]

    def str(self) -> str:
            return self.decompress()


# if __name__ == '__main__':  # Program will start here
#     from sys import getsizeof
#     original: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#     # print("original is {} bytes".format(getsizeof(original)))
#     # compressed: Compressed = Compressed(original) # compress
#     # print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
#     # print(compressed) # decompress
#     # print("original and decompressed are the same: {}".format(original ==
#     # compressed.decompress()))
#
#     print("Original size of {} bytes".format(getsizeof(original)))
#     compress: Compressed = Compressed(original)
#     print("Compressed Size of Original data is: {0} Bytes".format(getsizeof(compress.bit_string)))
#
#     print("Original and Decompressed are the same:", original == compress.decompress())