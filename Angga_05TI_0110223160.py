


list = ['mobil', 'scar', 2800, 'merah', 4]
list.append('3m')
list.append('48201')
list.insert(2, 'Ferrari')
print(list)

bangun_datar = int(input('Menghitung luas: '))

match bangun_datar:
    case 1: 
        sisi = int(input('Masukan sisi: '))
        rumus_p = sisi*sisi
        print('Luas Persegi adalah',(rumus_p))

    case 2:
        jari2=float(input('Masukan jari jari: '))
        luas_l = 3.14*jari2*jari2
        print('Luas Lingkaran Kamu adalah ', int(luas_l))
    case 3:
        alas = int(input('Masukan alas: '))
        tinggi = int(input('Masukan tinggi: '))
        rumus_segitiga = alas*tinggi/2
        print('Luas segitiga adalah', (alas,tinggi))
    case _:
        print('Kamu salah input')