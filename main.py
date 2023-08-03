import tkinter as tk

def calculate_cost():
    kilo_fiyati = float(kilo_fiyati_entry.get())
    gram_miktari = float(gram_miktari_entry.get())
    boyama_kalitesi = boyama_kalitesi_var.get()

    if boyama_kalitesi == "iyi":
        ek_fiyat = 0.55
    elif boyama_kalitesi == "orta":
        ek_fiyat = 0.35
    elif boyama_kalitesi == "kötü":
        ek_fiyat = 0.15
    elif boyama_kalitesi == "boyasiz":
        ek_fiyat = 0
    else:
        result_label.config(text="Hatalı bir değer girdiniz.")
        return

    flament_maliyeti = kilo_fiyati * gram_miktari / 1000
    toplam_maliyet = flament_maliyeti + (flament_maliyeti * ek_fiyat)

    if kar_alinacak_var.get():
        toplam_maliyet += 58
        
    if vernik.get():
        toplam_maliyet += 25

    result_label.config(text=f"Figürün maliyeti: {toplam_maliyet:.2f} TL.")

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("3D Figür Fiyat Hesaplama")

# Kilo fiyatı girişi
kilo_fiyati_label = tk.Label(root, text="Flamentin kilo fiyatını girin:")
kilo_fiyati_label.pack()
kilo_fiyati_entry = tk.Entry(root)
kilo_fiyati_entry.pack() 

# Gram miktarı girişi
gram_miktari_label = tk.Label(root, text="Figürde kullanılan flamentin gram miktarını girin:")
gram_miktari_label.pack()
gram_miktari_entry = tk.Entry(root)
gram_miktari_entry.pack()

# Boyama kalitesi seçimi
boyama_kalitesi_label = tk.Label(root, text="Figürün boyama kalitesini seçin:")
boyama_kalitesi_label.pack()

boyama_kalitesi_var = tk.StringVar(value="iyi")

iyi_radio = tk.Radiobutton(root, text="İyi", variable=boyama_kalitesi_var, value="iyi")
iyi_radio.pack()

orta_radio = tk.Radiobutton(root, text="Orta", variable=boyama_kalitesi_var, value="orta")
orta_radio.pack()

kotu_radio = tk.Radiobutton(root, text="Kötü", variable=boyama_kalitesi_var, value="kötü")
kotu_radio.pack()

boyasiz_radio = tk.Radiobutton(root, text="Boyasız", variable=boyama_kalitesi_var, value="boyasiz")
boyasiz_radio.pack()

# Kâr alınacak mı?
kar_alinacak_label = tk.Label(root, text="Kâr alınacak mı?")
kar_alinacak_label.pack()

kar_alinacak_var = tk.BooleanVar(value=False)

evet_radio = tk.Radiobutton(root, text="Evet", variable=kar_alinacak_var, value=True)
evet_radio.pack()

hayir_radio = tk.Radiobutton(root, text="Hayır", variable=kar_alinacak_var, value=False)
hayir_radio.pack()

# Vernik
vernik_label = tk.Label(root, text="Vernik Var mı?")
vernik_label.pack()

vernik = tk.BooleanVar(value=False)

evet_vernik_radio = tk.Radiobutton(root, text="Evet", variable=vernik, value=True)
evet_vernik_radio.pack()

hayir_vernik_radio = tk.Radiobutton(root, text="Hayır", variable=vernik, value=False)
hayir_vernik_radio.pack()


# Hesapla düğmesi
calculate_button = tk.Button(root, text="Hesapla", command=calculate_cost)
calculate_button.pack()

# Sonuç
result_label = tk.Label(root, text="")
result_label.pack()

isim_label = tk.Label(root, text="signed by quecy")
isim_label.pack();

# Pencereyi göster
root.mainloop();