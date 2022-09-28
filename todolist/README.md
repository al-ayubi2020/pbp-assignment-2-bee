# todolist

## assignment 4

[LINK](https://pbp-assignment-2-bee.herokuapp.com/todolist) atau https://pbp-assignment-2-bee.herokuapp.com/todolist

dummy account
username : pbp_user_1
password : pbp_user_1_password

username : pbp_user_2
password : pbp_user_2_password

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
