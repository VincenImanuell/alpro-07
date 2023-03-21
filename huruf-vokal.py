def hitung_vokal(kalimat):
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for karakter in kalimat:
        if karakter in vokal:
            jumlah = jumlah + 1
    return jumlah

def hitung_whitespace(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace() == True:
            jumlah = jumlah + 1
    return jumlah

def hitung_konsonan(kalimat):
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for karakter in kalimat:
        if karakter not in vokal and karakter.isalpha():
            jumlah = jumlah + 1
    return jumlah

# program utama
# input
kalimat = input('Masukkan sebuah kalimat : ')

# proses
jumlah_vokal = hitung_vokal(kalimat)
jumlah_whitespace = hitung_whitespace(kalimat)
jumlah_konsonan = hitung_konsonan(kalimat)

# output
print(f'Jumlah huruf vokal: {jumlah_vokal}')
print(f'Jumlah huruf whitespace: {jumlah_whitespace}')
print(f'Jumlah huruf konsonan: {jumlah_konsonan}')