import os
import sys
import time
import requests


def tam_otomatik_hatim():
  print("=" * 60)
  print("   OTOMATİK KESİNTİSİZ KUR'AN-I KERİM HATİM SİSTEMİ")
  print("=" * 60)

  print(
      "\n[Bilgi] Tüm Kur'an verisi sunucudan indiriliyor, bellek boyutu"
      " hesaplanıyor..."
  )

  baslangic_zamani = time.time()

  try:
    # Türkçe ve Arapça tüm Kur'an verisini çekiyoruz
    url_tr = "https://api.alquran.cloud/v1/quran/tr.yazir"
    res_tr = requests.get(url_tr)

    url_ar = "https://api.alquran.cloud/v1/quran/ar.alafasy"
    res_ar = requests.get(url_ar)

    # İndirilen ham JSON verisinin RAM'de kapladığı boyut (Byte ve Kilobyte/Megabyte cinsinden)
    json_boyutu_byte = len(res_tr.content) + len(res_ar.content)
    json_boyutu_kb = json_boyutu_byte / 1024
    json_boyutu_mb = json_boyutu_kb / 1024

    turkce_sureler = res_tr.json()["data"]["surahs"]
    arapca_sureler = res_ar.json()["data"]["surahs"]

    gecen_sure = time.time() - baslangic_zamani

    print(f"\n[SİSTEM BELLEK VE DEPOLAMA RAPORU]")
    print(f"--------------------------------------------------")
    print(f"• İndirilen Toplam Veri Boyutu (RAM / Ön Bellek): {json_boyutu_kb:.2f} KB ({json_boyutu_mb:.3f} MB)")
    print(f"• Veri İndirme Süresi: {gecen_sure:.2f} saniye")
    print(f"• Toplam Sure Sayısı: {len(turkce_sureler)}")
    print(f"--------------------------------------------------")
    print(
        "\nHiçbir tuşa basmanıza gerek kalmadan hatim başlatılıyor..."
        " (Durdurmak için Ctrl+C tuşlayın)\n"
    )
    time.sleep(3)

    # Sure sure döngü (1'den 114'e)
    for s_idx in range(len(turkce_sureler)):
      sure_adi = turkce_sureler[s_idx]["englishName"]
      sure_no = turkce_sureler[s_idx]["number"]
      tr_ayetler = turkce_sureler[s_idx]["ayahs"]
      ar_ayetler = arapca_sureler[s_idx]["ayahs"]

      print(
          f"\n\n============================================================"
      )
      print(f"   SURE {sure_no}: {sure_adi} (Toplam {len(tr_ayetler)} Ayet)")
      print(
          f"============================================================"
      )

      # Ayet ayet kesintisiz akış
      for i in range(len(tr_ayetler)):
        ayet_no = tr_ayetler[i]["numberInSurah"]
        meal = tr_ayetler[i]["text"]
        ses_url = ar_ayetler[i]["audio"]

        print(f"\n[{sure_no}. Sure - {ayet_no}. Ayet]")
        print(f"Meal: {meal}")
        print(">> Sesli okunuyor...")

        # Ses dosyası çalınır ve bitene kadar sonraki satıra geçmez
        os.system(f"mpv --no-video '{ses_url}' > /dev/null 2>&1")

  except KeyboardInterrupt:
    print(
        "\n\nHatim kullanıcı tarafından güvenle durduruldu. Allah kabul"
        " etsin."
    )
  except Exception as e:
    print(f"\nBir hata oluştu: {e}")


if __name__ == "__main__":
  tam_otomatik_hatim()

