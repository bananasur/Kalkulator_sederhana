import os

class SimpleCalc:
     
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pertambahan(self, a, b):
        return a + b 
    
    def pengurangan(self, a, b):
        return a - b
    
    def perkalian(self, a, b):
        return a * b
    
    def pembagian(self, a, b):
        return a / b

    
    def jalan(self):
        on = True
        while on:
            self.clear()
            print("==== MENU KALKULATOR SEDERHANA SURYA ====")
            print("1: Pertambahan")
            print("2: Pengurangan")
            print("3: Perkalian")
            print("4: Pembagian")
            print("5: Exit")
            print("Silakan pilih antara [1] [2] [3] [4] [5]")
            pilihan = input("Pilihan Anda: ")
            
            if pilihan == "5":
                on = False
                continue

            self.clear()
            a = int(input("Masukkan angka pertama: "))
            b = int(input("Masukkan angka kedua: "))

            if pilihan == "1":
                hasil = self.pertambahan(a, b)
                print(f"Hasil pertambahan: {hasil}")
            elif pilihan == "2":
                hasil = self.pengurangan(a, b)
                print(f"Hasil pengurangan: {hasil}")
            elif pilihan == "3":
                hasil = self.perkalian(a, b)
                print(f"Hasil perkalian: {hasil}")
            elif pilihan == "4":
                if b != 0:
                    hasil = self.pembagian(a, b)
                    print(f"Hasil pembagian: {hasil}")
                else:
                    print("Tidak dapat melakukan pembagian dengan angka 0.")
            else:
                print("Pilihan tidak valid!")
            
            input("Tekan enter untuk melanjutkan...")


kalkulator = SimpleCalc()
kalkulator.jalan()
