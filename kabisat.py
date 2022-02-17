def tahun_kabisat(a):
    if a % 4 == 0:
        return True
    else:
        return False

tahun = int(input("Masukkan Tahun :"))

if tahun_kabisat(tahun):
    print("Tahun ini adalah tahun kabisat")
else:
    print("Tahun ini bukan tahun kabisat")