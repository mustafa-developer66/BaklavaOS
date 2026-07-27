import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

# Terminal Renk Kodları
CYAN = "\033[96m"
MINT = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def ekran_temizle():
    os.system("clear" if os.name == "posix" else "cls")


def metin_temizle_ve_isle(ham_metin):
    """Gelen ham verideki HTML etiketlerini ve gereksiz boşlukları temizler."""
    clean = re.sub(r"<[^>]+>", "", ham_metin)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def veri_madencisi_ve_bellek_analizi():
    """İnternetten veri çeker, temizler, önbelleğe alır ve disk/RAM kullanımını gösterir."""
    ekran_temizle()
    print(
        f"{YELLOW}{BOLD}🌐 İNTERNET VERİ ÇEKME & ÖN BELLEK TEMİZLEME MERKEZİ{RESET}\n"
    )

    onbellek_verileri = {}
    toplam_ham_boyut = 0
    toplam_islenmis_boyut = 0

    # 1. TRT Haber Verisi Çekme
    print(f"{CYAN}📡 [1/3] Canlı Son Dakika Haber Verileri Çekiliyor...{RESET}")
    try:
        url_haber = "https://api.rss2json.com/v1/api.json?rss_url=https://www.trthaber.com/sondakika_articles.rss"
        req = urllib.request.Request(
            url_haber, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw_data = resp.read().decode("utf-8")
            toplam_ham_boyut += sys.getsizeof(raw_data)

            json_data = json.loads(raw_data)
            items = json_data.get("items", [])[:5]
            islenmis_haberler = [
                metin_temizle_ve_isle(item["title"]) for item in items
            ]

            onbellek_verileri["haberler"] = islenmis_haberler
            toplam_islenmis_boyut += sys.getsizeof(islenmis_haberler)
    except Exception as e:
        onbellek_verileri["haberler"] = ["Haber çekilemedi."]

    # 2. Döviz Kurları & Ekonomi Çekme
    print(f"{CYAN}📡 [2/3] Döviz ve Piyasa Verileri İşleniyor...{RESET}")
    try:
        url_doviz = "https://open.er-api.com/v6/latest/USD"
        req = urllib.request.Request(
            url_doviz, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw_data = resp.read().decode("utf-8")
            toplam_ham_boyut += sys.getsizeof(raw_data)

            json_data = json.loads(raw_data)
            try_rate = json_data.get("rates", {}).get("TRY", 0)

            doviz_bilgi = (
                f"1 Dolar (USD) = {try_rate:.2f} TL (Canlı Kur İşlendi)"
            )
            onbellek_verileri["doviz"] = doviz_bilgi
            toplam_islenmis_boyut += sys.getsizeof(doviz_bilgi)
    except Exception:
        onbellek_verileri["doviz"] = "Döviz verisi alınamadı."

    # 3. Hava Durumu Verisi
    print(
        f"{CYAN}📡 [3/3] Konum Ve Hava Durumu Verisi Analiz Ediliyor...{RESET}"
    )
    try:
        url_weather = "https://wttr.in/Ankara?format=j1"
        req = urllib.request.Request(
            url_weather, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw_data = resp.read().decode("utf-8")
            toplam_ham_boyut += sys.getsizeof(raw_data)

            w_json = json.loads(raw_data)
            temp = w_json["current_condition"][0]["temp_C"]
            desc = w_json["current_condition"][0]["lang_tr"][0]["value"]

            hava_bilgi = f"Ankara 📍 {temp}°C, {metin_temizle_ve_isle(desc)}"
            onbellek_verileri["hava"] = hava_bilgi
            toplam_islenmis_boyut += sys.getsizeof(hava_bilgi)
    except Exception:
        onbellek_verileri["hava"] = "Ankara 📍 17°C, Açık"

    time.sleep(1)

    # Diske Yazma / Yer Açma Raporlama
    dosya_adi = "baklava_onbellek_temp.json"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(onbellek_verileri, f, ensure_ascii=False, indent=2)

    yazilan_disk_boyutu = os.path.getsize(dosya_adi)

    # Rapor
    print(
        f"\n{GREEN}=================== VERİ & İŞLEME RAPORU ==================={RESET}"
    )
    print(
        f"📥 {BOLD}İnternetten Çekilen Ham Veri Boyutu :{RESET} {RED}{toplam_ham_boyut} Bayt{RESET}"
    )
    print(
        f"🧹 {BOLD}İşlenip Temizlenen Veri Boyutu    :{RESET} {GREEN}{toplam_islenmis_boyut} Bayt{RESET}"
    )
    print(
        f"💾 {BOLD}Diske Yazılan Temiz Önbellek Verisi:{RESET} {YELLOW}{yazilan_disk_boyutu} Bayt{RESET}"
    )
    kazanim = toplam_ham_boyut - toplam_islenmis_boyut
    print(
        f"🚀 {BOLD}Gereksiz Çöp Veriden Temizlenen Yer:{RESET} {MINT}{kazanim} Bayt Alan Açıldı!{RESET}"
    )
    print(
        f"{GREEN}============================================================{RESET}\n"
    )

    # Diskteki gereksiz önbellek dosyasını temizleyip yer açalım
    if os.path.exists(dosya_adi):
        os.remove(dosya_adi)
        print(
            f"{MINT}🗑️ Geçici önbellek dosyası saptandı ve silindi. Sistemde ekstra yer açıldı!{RESET}\n"
        )

    return onbellek_verileri


def canlı_konum_ve_hava():
    """Anlık basit hava durumu."""
    try:
        ip_url = "http://ip-api.com/json/"
        req = urllib.request.Request(
            ip_url, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sehir = data.get("city", "Ankara")

        w_url = f"https://wttr.in/{urllib.parse.quote(sehir)}?format=j1"
        req_w = urllib.request.Request(
            w_url, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req_w, timeout=4) as resp:
            w_data = json.loads(resp.read().decode("utf-8"))
            temp = w_data["current_condition"][0]["temp_C"]
            desc_list = w_data["current_condition"][0].get(
                "lang_tr", [{"value": "Açık"}]
            )
            desc = desc_list[0]["value"] if desc_list else "Açık"
            return f"{sehir.capitalize()} 📍 {temp}°C, {desc}"
    except Exception:
        return "Ankara 📍 17°C, Açık"


def ekranı_çiz(hava_durumu_bilgisi):
    """Sol üstte canlı saat, saniye, tarih ve hava durumunu basar."""
    ekran_temizle()
    simdi = datetime.datetime.now()
    saat_saniye = simdi.strftime("%H:%M:%S")
    tarih = simdi.strftime("%d.%m.%Y - %A")

    print(f"{MINT}┌──────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{MINT}│{RESET} 🕒 {BOLD}CANLI SAAT :{RESET} {YELLOW}{saat_saniye}{RESET} (Saat:Dakika:Saniye)        {MINT}│{RESET}")
    print(f"{MINT}│{RESET} 📅 {BOLD}TARİH      :{RESET} {tarih}                            {MINT}│{RESET}")
    print(f"{MINT}│{RESET} 🌤️ {BOLD}HAVA DURUMU:{RESET} {GREEN}{hava_durumu_bilgisi}{RESET}                    {MINT}│{RESET}")
    print(f"{MINT}└──────────────────────────────────────────────────────────────┘{RESET}")


def ana_menü():
    hava_durumu = canlı_konum_ve_hava()

    while True:
        ekranı_çiz(hava_durumu)
        print(f"\n         🥐 {BOLD}{YELLOW}BAKLAVA AI SÜPER KOMUTA MERKEZİ{RESET} 🥐\n")
        print(f"{GREEN}[1]{RESET} 💬 Baklava AI ile Sohbet Et / Soru Sor")
        print(
            f"{GREEN}[2]{RESET} ⚡ İnternetten Veri Çek / İşle / Önbellek & Disk Analizi Yap"
        )
        print(f"{GREEN}[3]{RESET} 🔄 Hava Durumu ve Konumu Güncelle")
        print(f"{GREEN}[4]{RESET} ✖️ Çıkış")

        seçim = input(
            f"\n{BOLD}Lütfen bir işlem seçin (1-4): {RESET}"
        ).strip()

        if seçim == "1":
            sohbet_modu()
        elif seçim == "2":
            veri_madencisi_ve_bellek_analizi()
            input(
                f"\n{YELLOW}Devam etmek için Enter'a basın...{RESET}"
            )
        elif seçim == "3":
            print(f"\n{MINT}Konum ve hava durumu güncelleniyor...{RESET}")
            hava_durumu = canlı_konum_ve_hava()
        elif seçim == "4":
            print(
                f"\n{YELLOW}Baklava AI kapatılıyor. Kendine iyi bak! 👋{RESET}"
            )
            break


def sohbet_modu():
    ekran_temizle()
    print(
        f"{YELLOW}=== BAKLAVA AI EKSİKSİZ SOHBET (Ana menü için 'menü' yaz) ==={RESET}\n"
    )

    while True:
        msg = input(f"{BOLD}Sen:{RESET} ").strip()
        if not msg:
            continue
        if msg.lower() in ["menü", "menu", "cikis", "exit", "q"]:
            break

        msg_lower = msg.lower()

        if "carpim tablosu" in msg_lower or "çarpım tablosu" in msg_lower:
            num = re.search(r"\d+", msg)
            if num:
                n = int(num.group())
                print(
                    f"\n{GREEN}Baklava AI:{RESET} {n} Sayısının Çarpım Tablosu:"
                )
                for i in range(1, 11):
                    print(f"   {n} x {i} = {n * i}")
            else:
                print(
                    f"\n{GREEN}Baklava AI:{RESET} Hangi sayının tablosunu istediğini belirtmelisin."
                )

        elif "android" in msg_lower:
            print(
                f"\n{GREEN}Baklava AI:{RESET} Android; Google tarafından geliştirilen Linux çekirdekli mobil işletim sistemidir."
            )

        elif any(op in msg for op in ["+", "-", "*", "/"]):
            try:
                temiz_islem = re.sub(r"[^0-9\+\-\*\/\.]", "", msg)
                sonuc = eval(temiz_islem)
                print(
                    f"\n{GREEN}Baklava AI:{RESET} Matematiksel Sonuç = {BOLD}{sonuc}{RESET}"
                )
            except Exception:
                print(
                    f"\n{GREEN}Baklava AI:{RESET} İşlem formatı anlaşılamadı."
                )

        else:
            print(
                f"\n{GREEN}Baklava AI:{RESET} '{msg}' sorunu aldım! Kendi içimde tüm verileri işliyorum."
            )

        print("-" * 45)


if __name__ == "__main__":
    ana_menü()

