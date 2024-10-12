# 403 Bypasser - VesperaIX

<div align="center">
  <img src="https://raw.githubusercontent.com/VesperaIX/Anti403/refs/heads/main/Anti%20403.png">
</div>
## Deskripsi
403 Bypasser adalah alat sederhana yang dirancang untuk mendeteksi kemungkinan bypass pada direktori yang memiliki izin akses 403 pada website. Dengan menggunakan berbagai payload, script ini melakukan pengujian untuk melihat apakah akses dapat diperoleh meskipun terdapat batasan pada server.

## Fitur
- Menghasilkan payload untuk mengakses direktori yang dibatasi.
- Mendeteksi status kode HTTP untuk setiap permintaan.
- Menampilkan status kode dengan warna yang berbeda untuk meningkatkan visibilitas:
  - **Hijau**: Status kode lain (selain 403 dan 404)
  - **Kuning**: Status kode 404
  - **Merah**: Status kode 403

## Prasyarat
- Python 3.x
- Pustaka `requests` dan `colorama` (dapat diinstal melalui pip)

## Instalasi
1. **Clone repository ini atau unduh script**:
   ```bash
   git clone https://github.com/VesperaIX/Anti403
   cd Anti403
   ```

2. **Instal dependensi**:
   ```bash
   sudo pip3 install requests colorama
   ```

## Penggunaan
Jalankan script dengan perintah berikut:
```bash
python3 bypass.py <target_url> <directory>
```

### Contoh:
```bash
python3 bypass.py https://example.com/ admin
```

**Catatan:**
- Pastikan URL diakhiri dengan `/`.
- Direktori tidak boleh diakhiri dengan `/`.

## Pesan
Saya tidak bertangung jawab atas kerusakan ataupun tindakan pengguna lain yang menggunakan alat ini, ini hanya untuk uji coba keamanan dan harus memiliki izin yang jelas jika ingin menerapkannya terhadap sistem orang lain

## Regards
VesperaIX
