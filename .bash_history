exit
cd
termux-setup-storage
cd /sdcard/ROM_KLASORUN/system/priv-app/
termux-setup-storage
cd /sdcard/GALAXY A3 2016 ROM VE TWRP
/system/priv-app/
cd /sdcard/GALAXY A3 2016 ROM VE TWRP
/system/priv-app/
cd "/sdcard/GALAXY A3 2016 ROM VE TWRP/system/priv-app/"
ls
find . -type d -exec chmod 755 {} \;
find . -type f -name "*.apk" -exec chmod 644 {} \;
​pkg update && pkg upgrade
apt update && apt upgrade -y
apt install git cmake clang python -y
apt install termux-tools -y
git clone [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
pkg install cmake -y
mkdir build
cd build
cmake ..
make
make clean
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j1
cmake .. -DGGML_CUDA=OFF -DGGML_CLBLAST=OFF -DGGML_VULKAN=OFF
cd ..
pkg install wget
wget [https://github.com/ggerganov/llama.cpp/releases/download/b3363/llama-b3363-bin-linux-aarch64.zip](https://github.com/ggerganov/llama.cpp/releases/download/b3363/llama-b3363-bin-linux-aarch64.zip)
pkg install wget
wget https://github.com/ggerganov/llama.cpp/releases/download/b3363/llama-b3363-bin-linux-aarch64.zip](https://github.com/ggerganov/llama.cpp/releases/download/b3363/llama-b3363-bin-linux-aarch64.zip
wget https://github.com/ggerganov/llama.cpp/releases/download/b3363/llama-b3363-bin-linux-aarch64.zip
pkg install llama.cpp
pkg install clang cmake make git python -y
pkg install libexecinfo -y
cd ~/llama.cpp
rm -rf build
mkdir build && cd build
cmake ..
make
pkg install llama-cpp
wget [https://github.com/ggerganov/llama.cpp/releases/latest/download/llama-cli-linux-aarch64](https://github.com/ggerganov/llama.cpp/releases/latest/download/llama-cli-linux-aarch64)
wget https://github.com/ggerganov/llama.cpp/releases/latest/download/llama-cli-linux-aarch64
pip install --upgrade pip
pkg install wget -y
pkg install llama.cpp -y
naber
Command pager in package w3m
pip install gradio requests
pkg install python-numpy clang -y
pip install gradio requests --no-build-isolation
pip install flask requests
nano app.py
python app.py
nano BaklavaAI.py
python BaklavaAI.py
pip install google-genai
nano BaklavaAI.py
python BaklavaAI.py
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
def yazdir_yavas(metin, hiz=0.01):
def dunya_saati_al(sehir_veya_ulke="turkiye"):
def wikipedia_ozet_al(sorgu):
def main():
if __name__ == "__main__":;     main() clear
clear
nano BaklavaAI.py
python BaklavaAI.py
nano BaklavaAI.py
python BaklavaAI.py
nano BaklavaAI.py
python BaklavaAI.py
nano BaklavaAI.py
python BaklavaAI.py
pip install streamlit
pkg update && apt list | wc -l
apt list | wc -l
pkg update -y && pkg install -y python python-pip clang make cmake git wget curl ffmpeg openssh nodejs rust golang zip unzip tar htop nano vim sqlite tesseract
pip install gradio
pkg install python nano -y
nano index.html
cat << 'EOF' > index.html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BaklavaOS - Geleceğin İşletim Sistemi</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background-color: #070a12; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; position: relative; }
        .glow-bg { position: absolute; top: -150px; left: 50%; transform: translateX(-50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(14, 116, 233, 0.25) 0%, rgba(7, 10, 18, 0) 70%); pointer-events: none; }
        .container { width: 100%; max-width: 900px; padding: 20px; z-index: 1; display: flex; flex-direction: column; align-items: center; }
        header { width: 100%; display: flex; justify-content: space-between; align-items: center; padding: 15px 0; margin-bottom: 40px; }
        .nav-logo { font-size: 24px; font-weight: 800; text-shadow: 0 0 20px rgba(14, 165, 233, 0.6); }
        .text-light-blue { color: #b9e6fe; }
        .text-blue { color: #0284c7; }
        .version-tag { background: rgba(14, 165, 233, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; }
        .hero { text-align: center; margin-bottom: 35px; }
        .main-title { font-size: 50px; font-weight: 900; letter-spacing: -1.5px; margin-bottom: 15px; }
        .subtitle { font-size: 16px; color: #94a3b8; max-width: 600px; line-height: 1.6; }
        .highlight-text { color: #38bdf8; font-weight: 600; }
        .terminal-box { width: 100%; max-width: 650px; background: #0d1322; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; overflow: hidden; margin-bottom: 45px; text-align: left; }
        .terminal-header { background: #131b2e; padding: 10px 15px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .dot { width: 12px; height: 12px; border-radius: 50%; }
        .dot-red { background-color: #ef4444; }
        .dot-yellow { background-color: #f59e0b; }
        .dot-green { background-color: #10b981; }
        .terminal-title { color: #64748b; font-size: 12px; font-family: monospace; margin-left: 10px; }
        .terminal-body { padding: 18px 20px; font-family: monospace; font-size: 14px; line-height: 1.7; }
        .cmd { color: #38bdf8; }
        .success { color: #10b981; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; width: 100%; margin-bottom: 50px; }
        .card { background: #0d1322; border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 16px; padding: 24px; }
        .card-icon { font-size: 28px; margin-bottom: 15px; }
        .card-title { font-size: 18px; font-weight: 700; margin-bottom: 10px; color: #f1f5f9; }
        .card-desc { font-size: 14px; color: #64748b; line-height: 1.5; }
        .cta-container { margin-bottom: 60px; }
        .btn-primary { background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; border: none; padding: 16px 36px; font-size: 16px; font-weight: 700; border-radius: 30px; box-shadow: 0 0 25px rgba(2, 132, 199, 0.5); }
        footer { color: #475569; font-size: 13px; margin-bottom: 25px; text-align: center; }
    </style>
</head>
<body>
    <div class="glow-bg"></div>
    <div class="container">
        <header>
            <div class="nav-logo"><span class="text-light-blue">Baklava</span><span class="text-blue">OS</span></div>
            <div class="version-tag">v1.0-alpha</div>
        </header>
        <section class="hero">
            <h1 class="main-title"><span class="text-light-blue">Baklava</span><span class="text-blue">OS</span></h1>
            <p class="subtitle">Sınırsız performans, üstün güvenlik ve modern mimari ile hazırlanan <span class="highlight-text">Geleceğin İşletim Sistemi</span>.</p>
        </section>
        <div class="terminal-box">
            <div class="terminal-header">
                <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
                <span class="terminal-title">baklavaos-kernel-build.log</span>
            </div>
            <div class="terminal-body">
                <div><span class="cmd">$ baklavaos --status</span></div>
                <div><span class="success">[SUCCESS]</span> Çekirdek ve sistem modülleri derleniyor...</div>
                <div>&gt; BaklavaOS lansmana hazırlanıyor. Çok yakında burada!</div>
            </div>
        </div>
        <div class="features-grid">
            <div class="card"><div class="card-icon">⚡</div><h3 class="card-title">Ultra Hızlı Çekirdek</h3><p class="card-desc">Maksimum donanım verimliliği ve sıfır gecikme için optimize edilmiş özel mimari.</p></div>
            <div class="card"><div class="card-icon">🛡️</div><h3 class="card-title">Gelişmiş Güvenlik</h3><p class="card-desc">Korumalı bellek yönetimi ve izolasyon protokolleri ile tam güvenlik.</p></div>
            <div class="card"><div class="card-icon">🎨</div><h3 class="card-title">Akıcı Arayüz</h3><p class="card-desc">Göz yormayan, şık ve son teknoloji kullanıcı deneyimi.</p></div>
        </div>
        <div class="cta-container"><button class="btn-primary">Lansmandan Haberdar Ol</button></div>
        <footer>© 2026 BaklavaOS Projesi. Tüm Hakları Saklıdır.</footer>
    </div>
</body>
</html>
EOF

python -m http.server 8080
cp /sdcard/Download/257651.png logo.png
