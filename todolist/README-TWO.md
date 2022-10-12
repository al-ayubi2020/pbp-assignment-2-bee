# Assignment 6

## Perbedaan asynchronous programming dengan synchronous programming

Perbedaan utama dari asynchronous programming dengan synchronous programming adalah pada Synchronous programming semua tugas dikerjakan atau dijalankan sesuai urutan, ini merupakan tipe pemrograman yang umum. Pada sisi lainnya, Asynchronous programming, memungkinkan tugas dikerjakan dalam urutan apapun.

## Event-Driven Programming

paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), keluaran sensor, atau pesan yang lewat dari program atau utas lain. Pemrograman berbasis peristiwa adalah paradigma dominan yang digunakan dalam antarmuka pengguna grafis dan aplikasi lain (misalnya, aplikasi web JavaScript) yang berpusat pada melakukan tindakan tertentu dalam menanggapi masukan pengguna.

## penerapan asynchronous programming pada AJAX.

Ajax memungkinkan untuk menjalankan atau memberikan request kepada server tanpa mempengaruhi halaman web yang sedang dikunjungi. Ajax melakukan hal tersebut dibalik layar sehingga user dapat terus untuk menjelajahi halaman web tersebut selagi ajax melakukan transaksi dengan database atau server. Dengan begitu, Ajax merupakan asynchronous programming dikarenakan pekerjaan ajax dilakukan saat ada sinyal diberikan dan dilakukan serta diselesaikan kapan pun tanpa menunggu jalan program yang lain.

## cara mengimplementasikan checklist di atas

### AJAX GET

dalam mengimplementasi ajax get, harus membuat sebuah view untuk menghandle request data dan membalikkannya dalam bentuk json ataupun html (dalam hal ini json). lalu gunakan ajax dengan sintax `$.get` dan isi parameternya sesuai dengan yang diminta. setelah itu, data yang diterima dimasukan kedalam html dengan cara yang bervariasi.

### AJAX POST

Modal dibuat menggunakan daisy UI. dengan view yang sudah tersedia sebelumnya, dapat langsung dibuat sebuah ajax post dengan sintax `$.ajax` dan dengan method post dan isi parameterlainnya dengan benar. setelah itu, ajax akan merefer form dengan id dan saat disubmit, fungsi post akan berjalan secara asynchronous dan setelah selesai upload data akan diupdate juga secara asynchronous dengan AJAX GET.
