# Praktikum 8
# Program Data Mahasiswa menggunakan Class
Dengan ketentuan sebagai berikut
- Method tambah() untuk menambah data
- Method tampilkan() untuk menampilkan data
- Method hapus(nama) untuk menghapus data berdasarkan nama
- Method ubah(nama) untuk mengubah data berdasarkan nama

# Membuat Method __init_
Method __*init*__() berguna untuk melakukan inisialisasi pembuatan object dari class.
```bash
class UPB:
    def __init__(self):
        self.dataMhs = {
        'No':[],
        'Nama':[],
        'NIM':[],
        'Nilai Tugas':[],
        'Nilai UTS':[],
        'Nilai UAS':[],
        'Nilai Akhir':[]
        }
```

# Membuat Method tambah()
Berfungsi sebagai metode menambahkan data
```bash
def tambah (self,no):
        print("Silahkan Input Data Anda ")
        nama = input("Masukan Nama Mahasiswa : ")
        nim = input("Masukan Nim Mahasiswa : ")
        tugas = int(input("Masukan Nilai Tugas Mahasiswa : "))
        uts = int(input("Masukan Nilai UTS Mahasiswa : "))
        uas = int(input("Masukan Nilai UAS Mahasiswa : "))
        nilaiAkhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100

        self.dataMhs['No'].append(no)
        self.dataMhs['Nama'].append(nama)
        self.dataMhs['NIM'].append(nim)
        self.dataMhs['Nilai Tugas'].append(tugas)
        self.dataMhs['Nilai UTS'].append(uts)
        self.dataMhs['Nilai UAS'].append(uas)
        self.dataMhs['Nilai Akhir'].append(nilaiAkhir)
        print("Succes")
```
**Programnya akan seperti ini**
![image.png](ss/tmbh.png)

# Membuat Method tampil()
Berfungsi sebagai metode menampilkan data yang sudah diinput
```bash
def tampil(self):
        print('Tampilan Data Nilai Mahasiswa')
        print(tabulate(self.dataMhs,
                       headers=['No', 'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                       tablefmt='fancy_grid'))
```
**Programnya akan seperti ini**
![image.png](ss/tmpl.png)

# Membuat Method hapus()
Berfungsi sebagai metode menghapus data yang sudah diinputkan
```bash
def hapus(self, nama):
        if nama in self.dataMhs["Nama"]:
            namaIndex = self.dataMhs['Nama'].index(nama)
            del self.dataMhs['No'][namaIndex]
            del self.dataMhs['Nama'][namaIndex]
            del self.dataMhs['NIM'][namaIndex]
            del self.dataMhs['Nilai Tugas'][namaIndex]
            del self.dataMhs['Nilai UTS'][namaIndex]
            del self.dataMhs['Nilai UAS'][namaIndex]
            del self.dataMhs['Nilai Akhir'][namaIndex]
            print("Data Was Deleted")
        else:
            print("Data Was Not Found")
```
**Programnya akan seperti ini**
![image.png](ss/hps.png)

# Membuat Method ubah()
```bash
def hapus(self, nama):
        if nama in self.dataMhs["Nama"]:
            namaIndex = self.dataMhs['Nama'].index(nama)
            del self.dataMhs['No'][namaIndex]
            del self.dataMhs['Nama'][namaIndex]
            del self.dataMhs['NIM'][namaIndex]
            del self.dataMhs['Nilai Tugas'][namaIndex]
            del self.dataMhs['Nilai UTS'][namaIndex]
            del self.dataMhs['Nilai UAS'][namaIndex]
            del self.dataMhs['Nilai Akhir'][namaIndex]
            print("Data Was Deleted")
        else:
            print("Data Was Not Found")
```
**Programnya akan seperti ini**
![image.png](ss/ubh.png)
**Data setelah kita ubah Nim-nya**
![image.png](ss/hslubh.png)

# Membuar Instance class untuk perulangan serta pemanggilan Method kembali
```bash
no = 0
instanceUPB = UPB()
loop = True
def judul():
    print("==============================")
    print("| Selamat Datang Di Aplikasi |")
    print("|   Input Nilai Mahasiswa    |")
    print("==============================")
    print("|1.|   Tambah Data           |")
    print("|2.|   Tampilkan Data        |")
    print("|3.|   Hapus Data            |")
    print("|4.|   Ubah Nama & Nilai     |")
    print("|5.|   Cari Nama Mahasiswa   |")
    print("|0.|   Keluar                |")
    print("==============================")

while loop:
    judul()
    menu = input("Masukan Pilihan : ")
    if menu == "1":
        while True :
            no += 1
            instanceUPB.tambah(no)
            tambahdata = input("Ingin Menambahkan Lagi ? (y/n) ")
            if tambahdata == "n":
                break
    elif menu == "2":
        instanceUPB.tampil()
        print(" ")
    elif menu == "3":
        print(tabulate(instanceUPB.dataMhs,
                   headers=['No', 'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                   tablefmt='fancy_grid'))
        nama = input("Pilih Data Nama Yang Ingin Dihapus : ")
        instanceUPB.hapus(nama)
    elif menu == "4":
        print(tabulate(instanceUPB.dataMhs,
                   headers=['No', 'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                   tablefmt='fancy_grid'))
        nama = input("Masukan Nama Yang Ingin Di Edit : ")
        print("==========================")
        instanceUPB.ubah(nama)
    elif menu == "0":
        print("|============================================|")
        print("| Terima Kasih Telah Menggunakan Program Ini |")
        print("|============================================|")
loop = False
```

# def judul()*
**Di dalam Instance class ada method def judul(), fungsinya ketika kita memanggil menu atau looping dari menu sebelumnya maka akan keluar judul yang berisikan menu-menu diatas**