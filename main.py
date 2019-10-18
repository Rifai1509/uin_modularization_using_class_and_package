nama ='Rifai'
program ='GLBB'
print(f'program {program} oleh {nama}')

# Vt = V0 + at
def hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + (percepatan*waktu)
    print(f'kecepatan awal = {kecepatan_awal} m/s dengan percepatan = {percepatan} m/s^2 ditempuh dalam waktu ={waktu} detik')
    print(f'sehingga kecepatan akhir={kecepatan_akhir} m/s')
    return kecepatan_akhir
hitung_kecepatan_akhir(5, 10, 30)

# s = V0 + 1/2 at^2
def hitung_jarak_tempuh(kecepatan_awal, percepatan, waktu):
    jarak_tempuh = kecepatan_awal + (1/2)*percepatan*(waktu**2)
    print(f'kecepatan awal = {kecepatan_awal} m/s dengan percepatan = {percepatan} m/s^2 ditempuh dalam waktu = {waktu} detik')
    print(f'sehingga jarak tempuhnya {jarak_tempuh} m')
hitung_jarak_tempuh(10,3,10)


# Vt^2 = V0^2 + 2as
def hitung_kecepatan_akhir_kuadrat(kecepatan_awal, percepatan, jarak_tempuh):
    kecepatan_akhir_kuadrat = kecepatan_awal**2 + 2*percepatan*jarak_tempuh
    print(f'kecepatan awal = {kecepatan_awal} m/s dengan percepatan = {percepatan} m/s^2 ditempuh dalam jarak = {jarak_tempuh} m')
    print(f'sehingga kecepatan akhir kuadrat {kecepatan_akhir_kuadrat} (m/s)^2')
hitung_kecepatan_akhir_kuadrat(10,2,50)