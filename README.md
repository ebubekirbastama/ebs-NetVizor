🌐 EBS-NetVizor

Windows platformu için geliştirilmiş, gerçek zamanlı ağ trafiği analiz aracı.  
PyQt5 tabanlı modern grafik arayüzü ile kullanıcıların paketleri, protokolleri, portları ve uygulama bazlı trafiği kolayca takip etmesine olanak sağlar. IP coğrafi konum entegrasyonu sayesinde hedef IP’lerin dünya üzerindeki konumu da görüntülenebilir.

---

🚀 Özellikler

- Canlı paket yakalama ve analiz (TCP, UDP, ICMP dahil)  
- Protokol ve port bazlı gelişmiş filtreleme  
- Uygulama bazlı (PID & program adı) aktif bağlantı takibi  
- Hedef IP’lerin coğrafi konum bilgisi (şehir, ülke)  
- Modern ve sezgisel PyQt5 grafik arayüzü  
- Canlı trafik grafikleri ile anlık veri takibi  

---

⚙️ Kurulum

1. Python 3.8 veya üzeri yüklü olmalı  
2. Windows işletim sistemi (WinDivert veya Npcap yüklü olmalı)  
3. Gerekli Python paketlerini yükleyin:

pip install pydivert PyQt5 matplotlib psutil requests

---

🛠️ Kullanım

Projeyi klonlayın veya zip olarak indirin, ardından:

python main.py

- Ana arayüzden protokol ve port bazlı filtrelemeyi aktif edebilirsiniz.  
- "Ağ Trafiği" sekmesinde paketleri ve canlı grafikleri görebilirsiniz.  
- "Uygulama Trafiği" sekmesinde hangi programların hangi bağlantıları kullandığını izleyebilirsiniz.  
- Hedef IP sütununda konum bilgisi görüntülenmektedir.  

---

📂 Proje Dosyaları

- main.py: Uygulama başlangıç noktası ve sniffer thread yönetimi  
- sniffer.py: Ağ paketlerini WinDivert ile yakalayan modül  
- ui_main.py: PyQt5 arayüzü, filtreleme ve tablolama  
- graph_panel.py: Canlı trafik grafik bileşeni  
- app_traffic.py: psutil ile uygulama bazlı aktif bağlantı bilgisi  
- geoip.py: IP adresinden konum bilgisi sorgulama  

---

💡 Geliştirme ve Katkı

Katkılar, hata bildirimleri ve geliştirme önerileri için pull request açabilirsiniz.  
Lütfen proje dizininde bulunan LICENSE dosyasını okuyunuz.

---

📜 Lisans

Apache License 2.0

Bu proje Apache License 2.0 altında lisanslanmıştır. Lisansın tam metni LICENSE dosyasında bulunmaktadır.

---

📞 İletişim

Sorularınız veya önerileriniz için:  
- Web Site: https://www.ebubekirbastama.com/ 
- GitHub: https://github.com/ebubekirbastama/ebs-NetVizo

---

EBS NetVizor ile ağınızı her an görün, kontrol sizde olsun! 🚦
