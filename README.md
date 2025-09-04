# Load Testing Tools

Ini merupakan tools yang di gunakan untuk melakukan penetrasi pada serangan bot bersekala besar tools atau pada script ini hanya pengembangan sederhana dan dapat di gunakan untuk pengujian. Tools ini dapat di jalankan pada bash asalkan semua library sudah terinstall dengan baik maka tools dapat di jalankan. tools ddosbetaspekpok di kembang oleh saya yang berkolaborasi dengan AI untuk membuat uji penetrasi yang terinspirasi dari k6.

## ✨ Fitur
- Script berbasis **Python** untuk menjalankan uji beban sederhana.
- Script berbasis **JavaScript** untuk pengujian menggunakan `k6`.

## 🚀 Cara Menjalankan


### 1. Jalankan script `stressHong.js` dengan k6
Pastikan `k6` sudah terinstall:  
```bash
k6 run stressHong.js 
```

### 2. Jalankan script `ddosbetaspekpok.py`:  
```bash
python ddos_tester.py [URL] -t [THREADS] -d [DURATION] 
```
