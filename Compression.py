

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # начальная метка
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # сдвиг влево на 2 бита
            if nucleotide == "А":  # поменять 2 последних бита на 00
                self.bit_string |= "0b00"
            elif nucleotide == "С":  # поменять 2 последних бита на 01
                self.bit_string |= "0b01"
            elif nucleotide == "G":  # поменять 2 последних бита на 10
                self.bit_string |= "0b0"
            elif nucleotide == "Т":  # поменять 2 последних бита на 11
                self.bit_string |= "0b1"
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide)) 
            
                      
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):# -1 чтобы исключить метку
            bits: int = self .bit_string >> i & "0b1" # получить только 2 значимых бита
            if bits == "0b00":  # А
                gene += "А"
            elif bits == "0b01":  # с
                gene += "С"
            elif bits == "0b0":  # G
                gene += "G"
            elif bits == "0b1":  # т
                gene += "Т"
            else:
                raise ValueError("Invalid bts:{}".format(bits))
            return gene[::-1]  # [::-1] обращение строки посредством обратных срезов
            
            
    def __str__(self) -> str:  # представление строки в биде красивого вывода
        return self.decompress()
        if __name__ == '__main__':
            from sys import getsizeof
            original: str ="TAGGGAТТAACCGТТATATATATATAGCCATGGATCGAТТATATAGGGAТТAACCGТТATATATATATAGCCATGGATCGAТТATA" * 100
            print("original is {} bytes".format(getsizeof(original)))
            compressed: CompressedGene = CompressedGene(original) # сжатие
            print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
            print(compressed)  # распаковка
            print("original and decompressed are the same: {}".format(original == compressed.decompress()))
