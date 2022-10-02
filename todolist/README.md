# todolist

# assignment 4

[LINK](https://pbp-assignment-2-bee.herokuapp.com/todolist) atau https://pbp-assignment-2-bee.herokuapp.com/todolist

dummy account <br>
username : pbp_user_1 <br>
password : pbp_user_1_password <br>
<br>
username : pbp_user_2 <br>
password : pbp_user_2_password <br>

## Kegunaan CSRF Token

CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban.

## yang Terjadi jika Tidak Menggunakan {% csrf_token %} pada Form

Maka dengan mudah orang lain selain user memberikan request dan request tersut akan diterima begitu saja tanpa adanya validasi apakah itu user atau bukan. Sehingga menyebabkan perubahan data yang tidak diinginkan oleh user.

## Sedikit Penjelasan Mengenai CSRF

CSRF adalah sebuah serangan yang membuat pengguna internet tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. Sehingga, aplikasi tersebut mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet.

Secara umum, CSRF bekerja sebagai berikut:

1. Pertama, seorang pengguna internet dan server akan mengkonfirmasi session ID dari suatu halaman website.
2. Kemudian, penyerang akan melakukan phising alias mengirimkan pesan yang dapat meyakinkan pengguna internet untuk mengklik exploit URL yang dicantumkan.
3. Exploit URL sudah di injeksi dengan perintah apapun sesuai keinginan penyerang, misalnya perintah untuk mengubah password akun.
4. Password dari akun pengguna pun secara otomatis berubah, dan ketika pengguna internet tersebut logout dari akunnya, ia tidak akan bisa login kembali ke akunnya. Sebab penyerang sudah mengganti password Anda.

Namun, ada beberapa ketentuan agar serangan CSRF dapat berjalan dengan baik, yaitu:

1. Aplikasi website harus menggunakan session cookies agar malicious request terlihat seperti authentic request.
2. CSRF dapat berhasil hanya jika korban sedang aktif di dalam aplikasi website yang dijadikan target.
3. Penyerang harus menemukan nilai parameter HTTP yang tepat agar tidak ditolak oleh aplikasi website yang dijadikan target.

## Membuat Elemen Form Secara Manual

Ya, kita dapat membuat elemen form tanpa menggunakan {{ form.as_table }}. Bisa dilihat pada create.html. Buat form sebagai tag wrapper dengan method post. Lalu, masukan crsf_token setelah tag form. Tambahkan field yang sesuai dengan model DB. Terakhir, buat button dengan type submit agar ketika diklik akan melakukan request post dengan data yang sudah dimasukan.

## Alur Data

user akan melakukan penambahan data menggunakan form. Setelah form tersebut selesai melakukan request post, selanjutnya data tersebut akan tersimpan pada DB. Ketika kembali ke url utama, semua data telah diambil begitu pula dengan data yang baru ditambahkan.

## Cara Implementasi Berdasarkan Checklist

- jalankan `python manage.py startapp todolist` pada terminal.
- Tambahkan bebearapa path yang ingin digunakan pada todolist, lalu hubungkan `project_django/urls.py` dengan `todolist/urls.py`.
- Buat model sesuai spesifikasi field.
- Untuk implementasi login dan logout, buat fungsi tersebut pada `todolist/views.py` lalu proteksi autentikasi pada beberapa fungsi dengan menambahkan `@login_required(login_url='/todolist/login/')`.
- Tambahkan tombol untuk dapat menuju halaman buat task. Lalu, buat fungsi untuk menambahkan task pada `todolist/views.py`.

# Assignment 5

## Perbedaan dari Inline, Internal, dan External CSS

1. Internal CSS
   Kode CSS internal diletakkan di dalam bagian head pada halaman. Class dan ID bisa digunakan untuk merujuk pada kode CSS, namun hanya akan aktif pada halaman tersebut. CSS internal diletakkan di dalam tag style. <br>
   Manfaat internal CSS:

   - Perubahan hanya terjadi pada 1 halaman
   - Class dan ID bisa digunakan oleh internal stylesheet
   - Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.
     Kekurangan internal CSS:
   - Meningkatkan waktu akses website
   - Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

2. External CSS
   Salah satu cara yang paling nyaman untuk menambahkan CSS. Dengan cara tersebut, perubahan apapun yang Anda buat pada file CSS akan tampil pada website Anda secara keseluruhan. Caranya dengan menghubungkan file CSS ke HTML malalui tag link. <br>
   Manfaat External CSS:

   - Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
   - Kecepatan loading menjadi lebih cepat
   - File CSS yang sama bisa digunakan di banyak halaman.
     Kekurangan External CSS:
   - Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

3. Inline CSS
   Inline CSS digunakan untuk tag HTML tertentu. Atribut style digunakan untuk memberikan style ke tag HTML tertentu. <br>
   Manfaat Inline CSS:
   - Berguna jika Anda ingin menguji dan melihat perubahan
   - Berguna untuk perbaikan cepat
   - Permintaan HTTP yang lebih kecil
     Kekurangan inline CSS:
   - Inline CSS harus diterapkan pada setiap elemen

## Tag HTML5 yang diketahui.

1. Tag `<html>...</html>`
   Tag `<HTML>` tugasnya adalah sebagai root, maksudnya semua tag yang berada didalam tag `<HTML>` merupakan gambaran dari dokumen HTML.
2. Tag `<head>...</head>`
   Tag `<HEAD>` tugasnya adalah memberikan informasi tentang dokumen, maksudnya didalam tag `<head>` kita bisa menambahkan tag- tag yang biasanya digunakan untuk memberikan informasi berupa penulis, judul dokumen, kata kunci pada dokumen dan masih banyak lagi informasi yang bisa di tambahkan pada tag ini.
3. Tag `<title>...</title>`
   Tag `<TITLE>` tugasnya adalah memberikan informasi berupa judul dokumen HTML.
4. Tag `<body>...</body>`
   Tag `<BODY>` tugasnya adalah memberikan isi dari suatu dokumen yang akan ditampilkan oleh web browsernya.
5. Tag `<p>...</p>`
   Tag `<P>` tugasnya adalah untuk membuat sebuah paragraf.
6. Tag `<!-- komentar -->`
   Tag `<!-- komentar -->` tugasnya adalah memberikan komentar pada sebuah dokumen HTML, namun tulisan yang dimasukan dalam tag ini tidak akan terlihat pada Web browser saat dijalankan tetapi dapat dilihat pada source program.
7. Tag `<header>...</header>`
   Tag `<HEADER>` merupakan bagian kepala dari dukumen.
8. Tag `<footer>...</footer>`
   Tag `<FOOTER>` merupakan bagian catatan kaki yang dapat berisi informasi tentang penulis, informasi hak cipta, dll
9. Tag `<nav>...</nav>`
   Tag `<NAV>` merupakan bagian dari dokumen yang dimaksudkan untuk memudahkan dalam proses navigasi.

## CSS selector

1. Selektor Tag
   Selektor Tag disbut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag.
2. Selektor Class
   Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
3. Selektor ID
   Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja. Selektor ID ditandai dengan tanda pagar (#) di depannya.
4. Selektor Atribut
   Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
5. Selektor Universal
   Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.
6. Pseudo Selektor
   Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

- Pseudo-class
  contoh: :hover, :link, :visited, :active, :focus, :checked.
- Pseudo-element
  contoh: ::first-line, ::before, ::after, ::marker, ::placeholder.

## Cara Implementasi

Pada tugas kali ini, saya menggunakan tailwind sebagai stylesheet nya. jadi tidak perlu membuat file css lagi tapi sudah di sediakan oleh tailwind dengan cara menuliskan class sesuai dengan dokumentasi. Pada tailwind juga sudah mengusung mobile-first responsive. dengan demikian untuk menerapkan responsive sangat mudah dengan tailwind.
