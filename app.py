import random
import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

WEATHER_API_URL = "https://wttr.in/{}?format=j1"


def hava_durumu_al(sehir):
    try:
        response = requests.get(WEATHER_API_URL.format(sehir), timeout=5)
        if response.status_code == 200:
            data = response.json()
            temp_c = data["current_condition"][0]["temp_C"]
            desc = data["current_condition"][0]["lang_tr"][0]["value"]
            return float(temp_c), desc
    except Exception:
        pass
    return None, None


def tartismaci_yanit(mesaj):
    mesaj_lower = mesaj.strip().lower()
    sehirler = [
        "istanbul",
        "ankara",
        "izmir",
        "bursa",
        "antalya",
        "adana",
        "trabzon",
        "eskişehir",
        "konya",
        "samsun",
    ]
    tespit_edilen_sehir = None

    for s in sehirler:
        if s in mesaj_lower:
            tespit_edilen_sehir = s
            break

    if not tespit_edilen_sehir and (
        "hava" in mesaj_lower or "kaç derece" in mesaj_lower
    ):
        kelimeler = mesaj_lower.split()
        for k in kelimeler:
            if k not in ["hava", "nasıl", "kaç", "derece", "bugün", "şimdi"]:
                tespit_edilen_sehir = k
                break

    if tespit_edilen_sehir:
        temp, desc = hava_durumu_al(tespit_edilen_sehir)
        sehir_baslik = tespit_edilen_sehir.capitalize()

        if temp is not None:
            if temp < 10:
                tepki = f"{sehir_baslik} şu an {temp}°C ve '{desc}'. Donuyoruz resmen! Ama eminim yine 'Hava çok güzel, dışarı çıkalım' diye saçmalarsın."
            elif temp > 25:
                tepki = f"{sehir_baslik} {temp}°C! Hava '{desc}'. Pişiyoruz! Bu havada dışarı çıkmayı düşünmüyorsundur umarım?"
            else:
                tepki = f"{sehir_baslik} {temp}°C ve '{desc}'. Ne sıcak ne soğuk, tam senin gibi sıradan bir hava işte."
            return f"Bunu bile internetten aratmaya üşeniyorsun değil mi? Al bakayım:\n\n👉 {tepki}"
        else:
            return f"'{tespit_edilen_sehir}' diye bir yer bulamadım. Belki de doğru düzgün yazmayı öğrenmelisin?"

    tartisma_cumleleri = [
        "Söylediğin şeyin mantıklı bir açıklaması var mı, yoksa sadece konuşmak için mi konuşuyorsun?",
        "Bu konuda seninle aynı fikirde olmam imkansız. Hangi mantıkla bunu savunuyorsun?",
        "Bunu bana soracağına biraz araştırma yapsan daha faydalı olmaz mıydı?",
        "Hava durumunu sormayacaksan vaktimi alma lütfen. Çok 'meşgul' bir yapay zekayım ben.",
        "Seninle tartışmak isterdim ama argümanların o kadar zayıf ki sıkılıyorum.",
    ]
    return random.choice(tartisma_cumleleri)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tartışmacı Hava Botu</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background: #121212; color: white; padding: 20px; text-align: center; }
        .chat-box { max-width: 500px; margin: 0 auto; background: #1e1e1e; padding: 20px; border-radius: 10px; }
        input[type=text] { width: 70%; padding: 10px; border-radius: 5px; border: none; }
        button { padding: 10px 15px; border-radius: 5px; border: none; background: #ff4757; color: white; font-weight: bold; }
        .response { margin-top: 20px; padding: 15px; background: #2ed573; color: black; border-radius: 8px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>🤖 Tartışmacı Hava Botu</h2>
        <form method="POST">
            <input type="text" name="mesaj" placeholder="Örn: Ankara hava nasıl?" required>
            <button type="submit">Gönder</button>
        </form>
        {% if yanit %}
            <div class="response">{{ yanit }}</div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    yanit = None
    if request.method == "POST":
        kullanici_mesaji = request.form.get("mesaj")
        yanit = tartismaci_yanit(kullanici_mesaji)
    return render_template_string(HTML_TEMPLATE, yanit=yanit)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

