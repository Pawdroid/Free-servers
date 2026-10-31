# Panduan konfigurasi klien

Pilih klien terlebih dahulu, lalu periksa format masukannya. Tautan GitHub dan Cloudflare dalam proyek ini menyediakan langganan node URI/Base64 biasa yang sama untuk setiap bahasa; tautan tersebut bukan profil Clash/Mihomo YAML atau sing-box JSON native yang siap pakai.

Simpan URL langganan pribadi dan kredensial di perangkat Anda sendiri. Jangan kirimkan ke situs konversi publik. Jika diperlukan format lain, dapatkan profil yang kompatibel dari penyedia atau siapkan secara lokal sesuai dokumentasi konfigurasi resmi klien tujuan.

[v2rayN](#v2rayn)
[Clash Verge Rev](#clash-verge-rev)
[Hiddify](#hiddify)
[Clash Party](#clash-party)
[FlClash](#flclash)
[Karing](#karing)
[Throne](#throne)
[Surge Mac](#surge)
[Quantumult X](#quantumult-x)
[sing-box for Apple platforms](#sing-box)
[v2rayNG](#v2rayng)
[Clash Meta for Android](#clash-meta-android)
[Surfboard](#surfboard)
[NekoBox for Android](#nekobox-android)
[Shadowrocket](#shadowrocket)
[Stash](#stash)
[Loon](#loon)
[Egern](#egern)
[Streisand](#streisand)
[Potatso](#potatso)
[OpenClash](#openclash)
[PassWall2 / PassWall](#passwall)
[Nikki](#nikki)
[HomeProxy](#homeproxy)

<a id="v2rayn"></a>

## v2rayN

**Format impor:** URI / Base64

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Format impor:** Clash / Mihomo YAML

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Format impor:** URI / Base64 · Clash YAML · sing-box JSON

Klien ini dapat membaca beberapa format, tetapi gunakan metode impor URI/Base64 biasa untuk langganan proyek ini. Profil JSON native dan YAML tetap memiliki persyaratan masing-masing.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Format impor:** Clash / Mihomo YAML

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Format impor:** Clash / Mihomo YAML

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Format impor:** URI / Base64 · Clash YAML · sing-box JSON

Klien ini dapat membaca beberapa format, tetapi gunakan metode impor URI/Base64 biasa untuk langganan proyek ini. Profil JSON native dan YAML tetap memiliki persyaratan masing-masing.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Format impor:** URI / Base64 · sing-box JSON · Clash YAML proxies

Impor langganan mengekstrak node yang didukung; jangan menganggap aturan dan pengaturan lain dari profil asli akan dipertahankan.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Format impor:** Surge INI / Managed Profile

Gunakan konfigurasi Surge atau URL konfigurasi terkelola. Jangan menganggap langganan V2Ray umum sebagai konfigurasi Surge lengkap.

### Pengaturan cepat

1. Siapkan profil lengkap dalam format yang disebutkan di atas. Impor berkas lokal atau URL profil jarak jauh yang didukung klien, perbarui, lalu pilih profil tersebut. Jangan menganggap langganan node biasa atau konfigurasi aplikasi lain dapat saling menggantikan.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Format impor:** Quantumult X / server_remote

Quantumult X menggunakan konfigurasi sendiri dan sumber daya server jarak jauh; konfigurasi lengkap dan sumber daya node merupakan masukan yang berbeda.

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil lengkap dalam format yang disebutkan di atas. Impor berkas lokal atau URL profil jarak jauh yang didukung klien, perbarui, lalu pilih profil tersebut. Jangan menganggap langganan node biasa atau konfigurasi aplikasi lain dapat saling menggantikan.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Format impor:** sing-box JSON

### Pengaturan cepat

1. Siapkan profil sing-box JSON lengkap yang sesuai dengan versi core klien. Tambahkan sebagai profil lokal atau jarak jauh, lalu perbarui. Daftar URL node atau berkas Clash YAML tidak dapat digunakan sebagai sing-box JSON native.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Format impor:** URI / Base64

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Format impor:** Clash / Mihomo YAML

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Referensi teknis [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Format impor:** Surfboard / Surge profile

Gunakan konfigurasi Surge atau URL konfigurasi terkelola. Jangan menganggap langganan V2Ray umum sebagai konfigurasi Surge lengkap.

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil lengkap dalam format yang disebutkan di atas. Impor berkas lokal atau URL profil jarak jauh yang didukung klien, perbarui, lalu pilih profil tersebut. Jangan menganggap langganan node biasa atau konfigurasi aplikasi lain dapat saling menggantikan.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Format impor:** URI / Base64 · Clash proxies · sing-box outbounds

Impor langganan mengekstrak node yang didukung; jangan menganggap aturan dan pengaturan lain dari profil asli akan dipertahankan.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Format impor:** Shadowrocket subscriptions / profiles

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan langganan node atau konfigurasi node individual yang didukung aplikasi ini. Tambahkan melalui metode impor yang dijelaskan dalam dokumentasi aplikasi, perbarui langganan jika didukung, dan pastikan node muncul. Daftar node dan profil perutean lengkap merupakan masukan yang berbeda.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

- [Informasi produk resmi [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Format impor:** Stash / Clash YAML

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Format impor:** URI / Base64 · Loon configuration

Loon menggunakan format konfigurasi dan langganan node tersendiri. Periksa setiap protokol dan kolom, jangan menganggap kompatibilitas penuh dengan Surge atau Clash.

### Pengaturan cepat

1. Tambahkan URL node yang didukung atau langganan URI/Base64 biasa di bagian langganan/profil klien. Perbarui langganan dan pastikan node yang diharapkan muncul.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Format impor:** Egern Profile.yaml / proxies YAML

Egern YAML adalah format profil tersendiri, bukan Clash/Mihomo YAML.

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil lengkap dalam format yang disebutkan di atas. Impor berkas lokal atau URL profil jarak jauh yang didukung klien, perbarui, lalu pilih profil tersebut. Jangan menganggap langganan node biasa atau konfigurasi aplikasi lain dapat saling menggantikan.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Format impor:** Supported node configurations

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan langganan node atau konfigurasi node individual yang didukung aplikasi ini. Tambahkan melalui metode impor yang dijelaskan dalam dokumentasi aplikasi, perbarui langganan jika didukung, dan pastikan node muncul. Daftar node dan profil perutean lengkap merupakan masukan yang berbeda.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

- [Informasi produk resmi [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Format impor:** Mihomo / Clash YAML · supported node links

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Siapkan profil YAML lengkap yang kompatibel dengan Clash/Mihomo. Impor sebagai profil lokal atau jarak jauh, perbarui, lalu pilih profil tersebut. Langganan biasa di atas bukan profil YAML lengkap.
2. Jika profil menyediakan pilihan, pilih node atau grup proxy, lalu aktifkan mode proxy/VPN sesuai dokumentasi klien. Berikan izin VPN sistem operasi hanya kepada aplikasi resmi yang Anda instal. Setelah tersambung, pastikan akses benar-benar berfungsi.
3. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

- [Informasi produk resmi [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Format impor:** Clash / Mihomo YAML

### Pengaturan cepat

1. Sebelum memasang, periksa firmware, arsitektur CPU, paket yang diperlukan, dan memori yang tersedia. Cadangkan konfigurasi router dan pertahankan koneksi pengelolaan yang berfungsi. Impor hanya langganan/profil yang didukung, perbarui, pilih node atau grup keluar, lalu aktifkan plugin sesuai petunjuk resminya.
2. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Format impor:** Supported node URI subscriptions

Impor langganan mengekstrak node yang didukung; jangan menganggap aturan dan pengaturan lain dari profil asli akan dipertahankan.

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Sebelum memasang, periksa firmware, arsitektur CPU, paket yang diperlukan, dan memori yang tersedia. Cadangkan konfigurasi router dan pertahankan koneksi pengelolaan yang berfungsi. Impor hanya langganan/profil yang didukung, perbarui, pilih node atau grup keluar, lalu aktifkan plugin sesuai petunjuk resminya.
2. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Referensi teknis [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Format impor:** Mihomo YAML: proxies / proxy-providers

### Pengaturan cepat

1. Sebelum memasang, periksa firmware, arsitektur CPU, paket yang diperlukan, dan memori yang tersedia. Cadangkan konfigurasi router dan pertahankan koneksi pengelolaan yang berfungsi. Impor hanya langganan/profil yang didukung, perbarui, pilih node atau grup keluar, lalu aktifkan plugin sesuai petunjuk resminya.
2. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

[Panduan resmi [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Format impor:** HomeProxy node subscriptions

HomeProxy mengelola node dan langganan melalui antarmukanya sendiri. Periksa format yang didukung versi yang terpasang; penggunaan sing-box secara internal tidak berarti sembarang profil sing-box JSON lengkap dapat diimpor.

Panduan pengguna resmi masih terbatas; gunakan langkah pengaturan ringkas dan referensi format resmi yang telah diverifikasi di bawah ini.

### Pengaturan cepat

1. Sebelum memasang, periksa firmware, arsitektur CPU, paket yang diperlukan, dan memori yang tersedia. Cadangkan konfigurasi router dan pertahankan koneksi pengelolaan yang berfungsi. Impor hanya langganan/profil yang didukung, perbarui, pilih node atau grup keluar, lalu aktifkan plugin sesuai petunjuk resminya.
2. Jika pembaruan gagal, periksa URL, jaringan, dan kesalahan HTTP. Jika penguraian gagal, periksa format dan versi core. Jika impor berhasil tetapi koneksi gagal, perbarui dan coba node lain yang didukung, lalu periksa log kesalahan klien. Pembaruan atau uji latensi yang berhasil tidak menjamin ketersediaan maupun keamanan.

Periksa protokol yang didukung dan versi core yang terpasang; mengimpor node tidak menjamin seluruh aturan, pengaturan DNS, atau kolom lanjutan ikut dipindahkan.

Panduan ringkas ini mencakup format masukan yang telah diverifikasi dan alur dasar. Referensi teknis yang ditautkan bukan tutorial pengguna langkah demi langkah; nama elemen antarmuka dapat berbeda menurut versi.

- [Referensi teknis [English]](https://github.com/immortalwrt/homeproxy)
