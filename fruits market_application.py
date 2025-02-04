#Soal 4

# cara menggunakan manual

listBuah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000]
]

cart = []

while True :
    pilihanMenu = input('''
        Selamat Datang di Pasar Buah

        List Menu :
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            #print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
            print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')
    elif(pilihanMenu == '2') :

        namaBuah = input('Masukkan Nama Buah : ')
        stockBuah = int(input('Masukkan Stock Buah : '))
        hargaBuah = int(input('Masukkan Harga Buah : '))
        listBuah.append({
            'nama': namaBuah,
            'stock': stockBuah,
            'harga': hargaBuah
        })
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

    elif(pilihanMenu == '3') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
        indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
        del listBuah[indexBuah]
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

    elif(pilihanMenu == '4') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
        while True :
            indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
            qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
            if(qtyBuah > listBuah[indexBuah][2]) :
                print('Stock tidak cukup, stock {} tinggal {}'.format(listBuah[indexBuah]['nama'],listBuah[indexBuah]['stock']))
            else :
                cart.append({
                    'nama': listBuah[indexBuah][0], 
                    'qty': qtyBuah, 
                    'harga': listBuah[indexBuah][2], 
                    'index': indexBuah
                })
            print('Isi Cart :')
            print('Nama\t| Qty\t| Harga')
            for item in cart :
                print('{}\t| {}\t| {}'.format(item[0], item[1], item[2]))
            checker = input('Mau beli yang lain? (ya/tidak) = ')
            if(checker == 'tidak') :
                break

        print('Daftar Belanja :')
        print('Nama\t| Qty\t| Harga\t| Total Harga')
        totalHarga = 0
        for item in cart :
            print('{}\t| {}\t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
            totalHarga += item[1] * item[2]    
        while True :
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            jmlUang = int(input('Masukkan jumlah uang : '))
            if(jmlUang > totalHarga) :
                kembali = jmlUang - totalHarga
                print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
                for item in cart :
                    listBuah[item['index']]['stock'] -= item['qty']
                cart.clear()
                break
            elif(jmlUang == totalHarga) :
                print('Terima kasih')
                for item in cart :
                    listBuah[item['index']]['stock'] -= item['qty']
                cart.clear()
                break
            else :
                kekurangan = totalHarga - jmlUang
                print('Uang anda kurang sebesar {}'.format(kekurangan))
                
    elif(pilihanMenu == '5') :
        break

# cara menggunakan tabulate
print("Soal 4")
print()
from tabulate import tabulate

data = [
    ["Apel", 20, 10000],
    ["Jeruk", 15, 15000],
    ["Anggur", 25, 20000]
]

headers = ["Nama", "Stock", "Harga"]

# Generate and print the table
# print("Daftar Buah")
# print(tabulate(data, headers=headers, tablefmt="pipe"))

while True:
    print("List Menu\n 1. Menampilkan Daftar Buah\n 2. Menambah Buah\n 3. Menghapus Buah\n 4. Membeli Buah\n 5. Exit Program")
    print()
    angkamenu=int(input("Masukkan angka Menu yang ingin dijalankan : "))
    
    if angkamenu == 5:
        print()
        print("Terima Kasih!")
        break
    
    elif angkamenu==1:
        print()
        print("Daftar Buah")
        print(tabulate(data, headers=headers, tablefmt="pipe",showindex="always"))
        print()
    
    elif angkamenu==2:
        print()
        buahbaru=input("Masukkan Nama Buah : ").capitalize()
        stockbaru=int(input("Masukkan Stock Buah : "))
        hargabaru=int(input("Masukkan Harga Buah : "))
        print()
        print("Berhasil Diperbaharui!")
        print()
        
        data.append([buahbaru,stockbaru,hargabaru])
        print(tabulate(data, headers=headers, tablefmt="pipe",showindex="always"))
        print()
    
    elif angkamenu==3:
        print()
        buahhapus=int(input("Masukkan Index Buah yang akan dihapus : "))
        del data[buahhapus]
        print()
        print("Berhasil Diperbaharui!")
        print()
        print(tabulate(data, headers=headers, tablefmt="pipe",showindex="always"))
        print()
    
    elif angkamenu==4:
        
        listjumlah=[]

        for a in data:
            
            while True:
                jumlahbuah = int(input(f"Masukkan Jumlah {a[0]} : "))
                if jumlahbuah>a[1]:
                    print("Mohon Maaf pesanan melebihi stock")
                else:
                    listjumlah.append(jumlahbuah)
                    break
            
        #Untuk stok berkurang
        for a in range(len(data)):
            data[a][1]=data[a][1]-listjumlah[a]
        
        
        print("Detail Belanja")
        
        #jumlah belanja buah diappend ke dalam data ["apel",15,10000,5(jumlah beli)]
        for a in range(len(data)):
            data[a].append(listjumlah[a])

        totalharga=0
        for a in data:
            print(f"{a[0]} : {a[3]} x Rp.{a[2]} = Rp.{(a[3]*a[2])}")
            totalharga=totalharga+(a[3]*a[2])
        
        print()
        print("Total : Rp.",totalharga)

        while True:
            uang=int(input("Masukkan Jumlah Uang : Rp."))
            sisauang = uang - totalharga

            if sisauang<0:
                print(f"Mohon Maaf Saldo anda tidak cukup \n Uangnya kurang sebesar Rp.{abs(sisauang)}")
            else:
                for a in data:
                    a.pop() #biar jumlah belanja buah ga nyangkut di data ketika program diulang, hapus data index paling akhir
                
                print ("Terima Kasih!")
                if  sisauang > 0:
                    print(f"Uang kembali Anda : Rp.{sisauang}")
                break
            
            
            print()
        
        
    else:
        print()
        print("Angka yang dimasukkan tidak Valid!")
        print()