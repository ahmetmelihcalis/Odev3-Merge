def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def main():
    print(" ***HESAP MAKİNESİ***")
    sayi1 = float(input("1.Sayıyı Giriniz: "))
    sayi2 = float(input("2.Sayıyı Giriniz: "))
    print(f"Toplam: {topla(sayi1, sayi2)}")
    print(f"Fark: {cikar(sayi1, sayi2)}")
    print(f"Çarpım: {carp(sayi1, sayi2)}")

if __name__ == "__main__":
    main()
