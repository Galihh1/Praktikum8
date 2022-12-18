from tabulate import tabulate
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

    def tampil(self):
        print('Tampilan Data Nilai Mahasiswa')
        print(tabulate(self.dataMhs,
                       headers=['No', 'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                       tablefmt='fancy_grid'))

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

    def ubah(self, nama):
        if nama in self.dataMhs['Nama']:
            namaIndex = self.dataMhs['Nama'].index(nama)
            print("Pilih data yang ingin diubah : ")
            while True:
                print("1. NIM")
                print("2. Nama")
                print("3. Nilai Tugas")
                print("4. Nilai UTS")
                print("5. Nilai UAS")
                print("0. Simpan Perubahan dan Keluar")
                editApa = int(input(" Masukan Pilihan : "))
                print("")
                if editApa == 1:
                    newNim = int(input("Masukan Nim : "))
                    self.dataMhs['NIM'][namaIndex] = newNim
                elif editApa == 2:
                    newNama = input("Masukan Nama : ")
                    self.dataMhs['Nama'][namaIndex] = newNama
                elif editApa == 3:
                    newTugas = int(input("Masukan Nilai Tugas : "))
                    nilai_akhir = (newTugas * 30 / 100) + (self.dataMhs['UTS'][namaIndex] * 35 / 100) + (
                                self.dataMhs['UAS'][namaIndex] * 35 / 100)
                    self.dataMhs['Tugas'][namaIndex] = newTugas
                    self.dataMhs['Nilai Akhir'][namaIndex] = nilai_akhir
                elif editApa == 4:
                    newUTS = int(input("Masukan Nilai UTS"))
                    nilai_akhir = (self.dataMhs['Tugas'][namaIndex] * 30 / 100) + (newUTS * 35 / 100) + (
                                self.dataMhs['UAS'][namaIndex] * 35 / 100)
                    self.dataMhs['UTS'][namaIndex] = newUTS
                    self.dataMhs['Nilai Akhir'][namaIndex] = nilai_akhir
                elif editApa == 5:
                    newUAS = int(input("Masukn Nilai UAS : "))
                    nilai_akhir = (self.dataMhs['Tugas'][namaIndex] * 30 / 100) + (
                                self.dataMhs['UTS'][namaIndex] * 35 / 100) + (newUAS * 35 / 100)
                    self.dataMhs['UAS'][namaIndex] = newUAS
                    self.dataMhs['Nilai Akhir'][namaIndex] = nilai_akhir
                elif editApa == 0:
                    print("Perubahan data berhasil di simpan")
                    break
                else:
                    print("Data tidak ditemukan")

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

