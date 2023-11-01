#kalkulator sederhana
print("|============================================|")
print("|        PROGRAM KALKULATOR SEDERHANA        |")
print("|============================================|")
print("|============================================|")
print("|            Menu Pilihan : 1-4              |")
print("|============================================|")
print("|             1. Penjumlahan                 |")
print("|             2. Pengurangan                 |")
print("|             3. Perkalian                   |")
print("|             4. Pembagian                   |")
print("|============================================|")
pilihan = int(input(" Masukan Pilihan Anda :"))

#function match itu sama dengan penggunaan switch case
match pilihan:
    case 1:
       print("|============================================|")
       print("|                 Penjumlahan                |")
       print("|============================================|")
       bil_1 = int(input(" Masukan Bilangan Pertama : " ) )
       bil_2 = int(input(" Masukan Bilangan Kedua : " ) )
       hasil = int(bil_1) + (bil_2)
       print(" Hasil dari "+str(bil_1)+" + "+str(bil_2)+" adalah : " +str(hasil))
       print("|============================================|")
        
    case 2:
       print("|============================================|")
       print("|                 Pengurangan                |")
       print("|============================================|")
       bil_1 = int(input(" Masukan Bilangan Pertama : " ) )
       bil_2 = int(input(" Masukan Bilangan Kedua : " ) )
       hasil = int(bil_1) - (bil_2)
       print(" Hasil dari "+str(bil_1)+" - "+str(bil_2)+" adalah : " +str(hasil))
       print("|============================================|")
       
    case 3:
       print("|============================================|")
       print("|                 Perkalian                  |")
       print("|============================================|")
       bil_1 = int(input(" Masukan Bilangan Pertama : " ) )
       bil_2 = int(input(" Masukan Bilangan Kedua : " ) )
       hasil = int(bil_1) * (bil_2)
       print(" Hasil dari "+str(bil_1)+" * "+str(bil_2)+" adalah : " +str(hasil))
       print("|============================================|")
       
    case 4:
       print("|============================================|")
       print("|                 Pembagian                  |")
       print("|============================================|")
       bil_1 = int(input(" Masukan Bilangan Pertama : " ) )
       bil_2 = int(input(" Masukan Bilangan Kedua : " ) )
       hasil = int(bil_1) / (bil_2)
       print(" Hasil dari "+str(bil_1)+" % "+str(bil_2)+" adalah : " +str(hasil))
       print("|============================================|")
       
    case 5:
        print(" Pilihan Tidak Tersedia ")
        exit()
