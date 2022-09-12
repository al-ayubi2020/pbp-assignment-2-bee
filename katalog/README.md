## Assignment 2

(isi link heroku disini)

## Bagan
![Bagan](../static/diagram.png?raw=true)<br>
Request diberikan oleh user dalam bentuk URL lalu views akan menangkap request tersebut sesuai dengan route yang ditentukan. setelah diterima oleh views, views akan melakukan query kepada DB melalui file models. lalu, models akan melakukan transaksi dengan DB dan models akan memberikan respons yang sesuai kepada views. Respons diterima oleh views dan views akan mereturn data bertipe dictionary kepada template yang dipilih melalui fungsi render. Dan hasilnya, template akan terender di browser client.
<br>

## Virtual Environment
### Kenapa menggunakan virtual environment?
Hampir semua orang di komunitas pengguna python, menyarankan untuk menggunakan virtual environment dalam melakukan projek python manapun. Singkatnya, hal itu dikarenakan Python tidak bekerja dengan baik dalam hal mengatur depedencies. Jika kita tidak spesifik dalam menulis directory saat mengistal sebuah dependency, maka pip akan menempatkan semua paket eksternal yang kita instal di folder bernama site-packages/ di instalasi Python dasar kita. venv atau virtual environment dari python merupakan environtment manager yang membuat sebuah scope virtual yang terisolasi. venv ini akan mengisolasi packages dan dependancies yang ada di project. Saat kita membuat project, enc akan memastikan seluruh data yang ada di library project tidak akan berubah pada storage local kita dan hanya akan berubah di virtual environtment env.

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawabannya adalah bisa. Namun, membuat sebuah projek python tanpa virtual env memiliki resiko tersendiri. Yaitu, seiring berjalannya waktu, potensi munculnya konflik dependency semakin besar. Seperti yang kita tahu, jika tidak menggunakan virtual env, maka pip akan menempatkan semua paket eksternal yang kita instal di folder bernama site-packages/ di instalasi Python dasar kita. Meskipun demikian, mengembangkan projek django tanpa virtual environment sangat dimungkinkan, namun dengan risikonya sendiri.


## Implementasi views.py
Pertama, harus import database models dengan nama class CatalogItem dahulu dari models.py dari directory file yang sama, dengan demikian saya dapat berinteraksi dengan DB. Lalu, CatalogItem dapat mengambil data dari DB lalu disimpan pada sebuah variable bernama data_catalog. Setelah itu, membuat sebuah data bertipe directory yang bernama context dan berisi data_catalog tersebut dan beberapa data tambahan lainnya. Terakhir, buat sebuah fungsi bernama show_katalog dengan parameter request. Fungsi tersebut akan mereturn fungsi render dengan berisi parameter request, nama template ("katalog.html"), dan data dari DB yang telah kita masukan kedalam variable context. Fungsi show_katalog ini akan diimport dan dipanggil pada saat proses routing sesuai routes yang telah ditentukan yaitu "/katalog".

## Implementasi Routing
dalam routing, kita harus mendefinisikan sebuah route baru dalam file urls.py yang ada pada folder project_django dengan mengimport pula urls.py yang ada pada folder katalog. Pada proses routing ini, file urls.py pada folder katalog akan menginvoke fungsi show_catalog dan akhirnya akan merender data yang ada dalam context ke dalam katalog.html

## Implementasi Pemetaan Data Django ke Dalam Template HTML
pada saat routing, fungsi show_catalog mengirim data context kepada katalog.html. context merupakan data bertipe dictionary, jadi kita dapat memanggil key dari setiap value jika ingin menampilkan value tersebut kedalam file katalog.html. untuk value bertipe array kita dapat melakukan unboxing dengan melakukan loop.

## Implementasi Deployment ke Heroku
Buat aplikasi baru pada heroku, 
