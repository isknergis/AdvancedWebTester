# Advanced Web Tester  
## 📌 Web Güvenlik Test Aracı  

🔍 **Bu proje, web uygulamalarını güvenlik açıklarına karşı test etmek için geliştirilmiş bir otomatik tarama aracıdır.**  

---

## 🔍 Test Edilen Güvenlik Açıkları  
Bu araç, aşağıdaki güvenlik açıklarını tespit etmek için tasarlanmıştır:  

- **SQL Injection** → Hedef sistemin SQL sorgu manipülasyonlarına karşı açık olup olmadığını analiz eder.  
- **Cross-Site Scripting (XSS)** → Zararlı JavaScript kodlarının yürütülmesini test eder.  
- **Cross-Site Request Forgery (CSRF)** → Kullanıcı oturumu üzerinden yetkisiz işlem yapılmasını inceler.  
- **Local File Inclusion (LFI)** → Sunucu üzerindeki hassas dosyalara erişim olup olmadığını test eder.  
- **Remote File Inclusion (RFI)** → Uzaktan kötü amaçlı dosya çalıştırma riskini değerlendirir.  


## 🚀 Kurulum  
### 🔹 Bağımlılıkları yükleyin:  
```bash
pip install flask requests
python flask_app.py
http://127.0.0.1:5001
