from tabulate import tabulate

#Collection Data
data_mobil = {
    'AY01MT': {'Tipe': 'Ayla', 'Transmisi': 'MT', 'Seats': 5, 'Status' : 'Tersedia', 'Harga': 250000},
    'AV01MT': {'Tipe': 'Avanza', 'Transmisi': 'MT', 'Seats': 6, 'Status' : 'Disewakan', 'Harga': 370000},
    'EX01AT': {'Tipe': 'Expander', 'Transmisi':'AT', 'Seats': 6, 'Status' : 'Tersedia', 'Harga': 430000}
}

nama_kolom = ['ID Mobil', 'Tipe', 'Transmisi', 'Seats', 'Status', 'Harga']

#Print tabel data mobil
def cetak_data_mobil():
    if len(data_mobil) > 0:
        stok_mobil = []
        for i in data_mobil.keys():
            baris = [
                i, 
                data_mobil[i]['Tipe'], 
                data_mobil[i]['Transmisi'], 
                data_mobil[i]['Seats'], 
                data_mobil[i]['Status'], 
                data_mobil[i]['Harga']
            ]
            stok_mobil.append(baris)
        print(tabulate(stok_mobil, headers=nama_kolom, tablefmt="double_grid", stralign="center", numalign="center"))
    else:
        print('Tidak ada data tersimpan.')


#Cari data mobil berdasarkan ID
def cari_mobil(data_mobil): 
    if len(data_mobil) == 0:
        print('Tidak ada data tersimpan.')
    else:
        id_mobil = input('Masukkan ID mobil: ')
        if id_mobil in data_mobil.keys():
            mobil = data_mobil[id_mobil]
            hasil_pencarian = [
                [id_mobil, mobil['Tipe'], mobil['Transmisi'], mobil['Seats'], mobil['Status'], mobil['Harga']]
                ]
            headers = ['ID Mobil', 'Tipe', 'Transmisi', 'Seats', 'Status', 'Harga']
            print(tabulate(hasil_pencarian, headers=headers, tablefmt="double_grid", stralign="center", numalign="center"))
        else:
            print("Tidak ada mobil yang sesuai dengan kriteria yang diberikan.")


#Menu Read
def sub1_menu_read(): 
    while True:
        print('''
            Menu Tampilan Data Mobil:
            1. Tampilkan seluruh data mobil
            2. Tampilkan mobil berdasarkan kriteria
            3. Kembali ke Menu Utama
            ''')
        opsi_sub1 = input('Masukkan angka sesuai menu yang ingin dipilih: ')
        if opsi_sub1 == '1':
            cetak_data_mobil()
        elif opsi_sub1 == '2':
            cari_mobil(data_mobil)
        elif opsi_sub1 == '3':
            break
        else:
            print('Masukkan angka sesuai menu yang tersedia.')

sub1_menu_read()

# Memesan mobil rental
from datetime import datetime

def sub3_cust():
    while True:
        pesan_plat = input('Masukkan plat mobil yang ingin dipesan: ')
        if pesan_plat in data_mobil:
            print('Detail mobil yang ingin dipesan: ')
            print(tabulate([data_mobil[pesan_plat]], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
            check_1 = input('Apakah data mobil sudah sesuai? (ya/tidak): ').lower()  # checker
            if check_1 == 'ya':
                while True:
                    try:
                        tanggal_mulai = input('Masukkan tanggal mulai rental (DD-MM-YYYY): ')
                        tanggal_selesai = input('Masukkan tanggal selesai rental (DD-MM-YYYY): ')
                        tanggal_mulai_dt = datetime.strptime(tanggal_mulai, '%d-%m-%y')
                        tanggal_selesai_dt = datetime.strptime(tanggal_selesai, '%d-%m-%y')
                        if tanggal_selesai_dt <= tanggal_mulai_dt:
                            print('Tanggal selesai harus lebih besar dari tanggal mulai.')
                        break
                    except ValueError as e:
                        print(f'Tanggal tidak valid: {e}. Silakan coba lagi.')

                pesan_durasi = (tanggal_selesai_dt - tanggal_mulai_dt).days
                harga_per_hari = int(data_mobil[pesan_plat]['Harga'])
                total_biaya = harga_per_hari * pesan_durasi
                print(f'Biaya rental per hari: {harga_per_hari} \nLama rental: {pesan_durasi} hari')
                print(f'Total biaya rental: {total_biaya}')
                check_1 = input('Lanjutkan transaksi? (ya/tidak): ').lower()
                if check_1 == 'ya':
                    bayar = input('''
                                Metode pembayaran
                                1 : QRIS
                                2 : Transfer
                                Masukkan metode pembayaran Anda: ''')
                    if bayar == '1':
                        print('<barcode>')
                        print('Kirim bukti transfer ke WA: 082273858281 (Cahaya)')
                    elif bayar == '2':
                        print('Rek BRI an Cahaya Tambunan 01298020')
                        print('Kirim bukti transfer ke WA: 082273858281 (Cahaya)')
                    else:
                        print('Masukkan input yang sesuai.')
                else:
                    print('Transaksi dibatalkan.')
                break  # Kembali ke menu utama
            elif check_1 == 'tidak':
                opsi_1 = input('''
                    1. Kembali memilih plat
                    2. Kembali ke Menu Utama
                    Masukkan pilihan Anda: ''')
                if opsi_1 == '1':
                    continue  # Kembali ke loop awal untuk memilih plat
                elif opsi_1 == '2':
                    break  # Kembali ke menu utama
                else:
                    print('Masukkan input yang sesuai.')
            else:
                print('Masukkan input yang sesuai.')
        else:
            print(f'Tidak ada data mobil dengan plat {pesan_plat}.')
            break


#Fungsi untuk memeriksa validitas plat nomor
def is_valid_plate(plate):
    parts = plate.split()
    if len(parts) == 3 and parts[0].isalpha() and parts[1].isdigit() and parts[2].isalpha():
        if 1 <= len(parts[0]) <= 2 and 1 <= len(parts[1]) <= 4 and 1 <= len(parts[2]) <= 3:
            return True
    return False

#Menambah Data ke Daftar Mobil
def sub2_admin():
    while True:
        print('''
        Menu Menambah Data Mobil
        1: Menambah Data Mobil
        2: Keluar
            ''')
        opsi_sub2 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub2 == '1':
            print('\t Menambah Data Mobil')
            while True:
                plat_baru = input('Masukkan Nomor Plat: ').strip().upper()
                if is_valid_plate(plat_baru):
                    if plat_baru in data_mobil:
                        print('Data sudah ada.')
                    else:
                        merk_baru = input('Masukkan merk mobil: ').capitalize()
                        tipe_baru = input('Masukkan tipe mobil: ').capitalize()
                        
                        # Validasi transmisi
                        while True:
                            trans_baru = input('Masukkan transmisi mobil (AT/MT): ').strip().upper()
                            if trans_baru in ['AT', 'MT']:
                                break
                            else:
                                print("Transmisi tidak valid. Masukkan hanya 'AT' atau 'MT'.")
                        
                        # Validasi seats
                        while True:
                            try:
                                seats_baru = int(input('Masukkan jumlah seats mobil: '))
                                if seats_baru > 0 and seats_baru < 9:
                                    break
                                else:
                                    print("Jumlah seats harus lebih dari 0.")
                            except ValueError:
                                print("Seats harus berupa angka.")
                        
                        # Validasi harga
                        while True:
                            try:
                                harga_baru = int(input('Masukkan harga rental mobil/hari: Rp '))
                                if harga_baru > 100000 and harga_baru <1000000 and harga_baru% 1000 == 0:
                                    break
                                else:
                                    print("Harga harus lebih dari Rp 100000.")
                            except ValueError:
                                print("Harga harus berupa angka.")

                        #Membuat dictionary baru dengan plat_baru sebagai kunci
                        mobil_baru = {
                            'Merk': merk_baru,
                            'Tipe': tipe_baru,
                            'Transmisi': trans_baru,
                            'Seats': seats_baru,
                            'Plat': plat_baru,
                            'Harga': harga_baru
                        }

                        print("Data mobil baru:")
                        print(tabulate([mobil_baru], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        
                        while True:
                            checker_1 = input('Apakah anda yakin ingin menambahkan data mobil di atas? (ya/tidak): ').strip().lower()
                            if checker_1 == 'ya':
                                data_mobil[plat_baru] = mobil_baru
                                print('Data mobil berhasil ditambahkan.')
                                break
                            elif checker_1 == 'tidak':
                                print('Data mobil tidak ditambahkan.')
                                break
                            else:
                                print('Masukkan input yang sesuai YA atau TIDAK.')
                    break
                else:
                    print('Nomor plat tidak valid. \nContoh format yang benar: B 1234 XYZ')
        elif opsi_sub2 == '2':
            break
        else:
            print('Masukkan input yang sesuai')

def sub3_admin():
    while True:
        print('''
        Menu Update Data Mobil
        1: Update Data Mobil
        2: Cari Data Mobil
        3: Keluar
            ''')
        opsi_sub3 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub3 == '1':
            while True:
                index_mobil = input('Masukkan nomor plat mobil yang ingin diubah: ').strip().upper()
                if is_valid_plate(index_mobil):
                    if index_mobil in data_mobil:
                        print(tabulate([data_mobil[index_mobil]], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        checker_3 = input('Apakah anda yakin ingin mengubah data mobil tersebut? (ya/tidak): ').lower()
                        if checker_3 == 'ya':
                            updated_data = data_mobil[index_mobil].copy()  # Salin data ke variabel sementara
                            print(f'''\t Update Data Mobil {index_mobil}
                            1. Merk
                            2. Tipe
                            3. Transmisi
                            4. Jumlah Seats
                            5. Harga Rental
                            ''')
                            opsi_update = input('Masukkan opsi yang ingin diubah: ')
                            if opsi_update == '1':
                                updated_data["Merk"] = input('Masukkan Merk Mobil Terbaru: ')
                            elif opsi_update == '2':
                                updated_data["Tipe"] = input('Masukkan Tipe Mobil Terbaru: ')
                            elif opsi_update == '3':
                                updated_data["Transmisi"] = input('Masukkan Jenis Transmisi Terbaru: ')
                            elif opsi_update == '4':
                                while True:
                                    try:
                                        seats_baru = int(input('Masukkan Jumlah Seats Terbaru: '))
                                        if seats_baru > 0 and seats_baru < 9:
                                            updated_data["Seats"] = seats_baru
                                            break
                                        else:
                                            print("Jumlah seats harus lebih dari 0 dan kurang dari 9.")
                                    except ValueError:
                                        print("Seats harus berupa angka.")
                            elif opsi_update == '5':
                                while True:
                                    try:
                                        harga_baru = int(input('Masukkan harga rental mobil/hari: Rp '))
                                        if harga_baru > 100000:
                                            break
                                        else:
                                            print("Harga harus lebih dari Rp 100000.")
                                    except ValueError:
                                        print("Harga harus berupa angka.")
                            
                            print(tabulate([updated_data], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                            checker_4 = input('Apakah Anda yakin ingin memperbaharui data mobil sebagai data di atas? (ya/tidak): ').lower()
                            if checker_4 == 'ya':
                                data_mobil[index_mobil] = updated_data  # Simpan perubahan ke data asli
                                print('Data berhasil disimpan.')
                                break
                            elif checker_4 == 'tidak':
                                print('Data tidak disimpan.')
                                break
                            else:
                                print('Masukkan input yang sesuai.')
                        elif checker_3 == 'tidak':
                            break
                        else:
                            print('Masukkan input yang sesuai.')
                    else:
                        print('Nomor plat tidak ditemukan.')
                else:
                    print('Nomor plat tidak sesuai format. Contoh yang benar: B 1234 XYZ')
        elif opsi_sub3 == '2':
            cari_mobil(data_mobil)
        elif opsi_sub3 == '3':
            break
        else:
            print('Masukkan input yang sesuai.')


def sub4_admin():
    while True:
        print('''
        Menu Hapus Data Mobil
        1: Hapus Data Mobil
        2: Keluar
        ''')
        opsi_sub4 = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_sub4 == '1':
            while True:
                hapus_mobil = input('Masukkan nomor plat mobil yang ingin dihapus: ')
                if is_valid_plate(hapus_mobil):
                    if hapus_mobil in data_mobil:
                        print("Data mobil yang akan dihapus:")
                        print(tabulate([data_mobil[hapus_mobil]], headers="keys", tablefmt="double_grid", stralign="center", numalign="center"))
                        checker2 = input('Apakah Anda yakin ingin menghapus data mobil ini? (ya/tidak): ')
                        if checker2.lower() == 'ya':
                            del data_mobil[hapus_mobil]
                            print(f'Data mobil dengan nomor plat {hapus_mobil} telah dihapus.')
                            break
                        elif checker2.lower() == 'tidak':
                            print('Penghapusan dibatalkan.')
                            break
                        else:
                            print('Masukkan inputan yang sesuai.')
                    else:
                        print(f'Data mobil dengan plat {hapus_mobil} tidak ada.')
                        break
                else:
                    print('Nomor plat tidak valid. \nContoh format yang benar: B 1234 XYZ')
        elif opsi_sub4 == '2':
            break
        else:
            print('Masukkan input yang sesuai')

def keluar():
    print('Program berhenti.')

def menu_cust():
    while True:
        print('''
Menu Utama
1: Menampilkan Daftar Mobil
2: Menampilkan Daftar Mobil Berdasarkan Spesifikasi 
3: Memesan mobil
4: Keluar
        ''')
        opsi_menu_cust = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_menu_cust == '1':
            if len(data_mobil) == 0:
                print('Tidak ada data mobil tersimpan.')
            else:
                cetak_data_mobil()
        elif opsi_menu_cust == '2':
            cari_mobil(data_mobil)
        elif opsi_menu_cust == '3':
            sub3_cust()
        elif opsi_menu_cust == '4':
            keluar()
            break
        else:
            print('Masukkan inputan yang sesuai.')

def menu_admin ():
    while True:
        print('''
        Menu admin
        1: Menampilkan Data Mobil
        2: Menambahkan Data Mobil
        3: Mengupdate Data Mobil
        4: Delete Data Mobil
        5: Keluar
            ''')
        opsi_menu_admin = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_menu_admin == '1':
            sub1_admin()
        elif opsi_menu_admin =='2':
            sub2_admin()
        elif opsi_menu_admin == '3':
            sub3_admin()
        elif opsi_menu_admin == '4':
            sub4_admin()
        elif opsi_menu_admin == '5':
            print('Program berhenti.')
            break
        else:
            print('Masukkan angka sesuai menu yang tersedia.')

def menu_utama():
    while True:
        print('''
        Selamat Datang di Rental Pati
        Masuk Sebagai:
        1: Customer
        2: Admin
        3: Keluar
            ''')
        opsi_menu_utama = input('Pilih menu berdasarkan angka yang tertera: ')
        if opsi_menu_utama == '1':
            menu_cust()
        elif opsi_menu_utama =='2':
            menu_admin()
        elif opsi_menu_utama == '3':
            print('Program berhenti.')
            break
        else:
            print('Masukkan angka sesuai menu yang tersedia.')
