# mywatchlist

## Assignment 3

[HTML](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/html/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/html/

[JSON](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/json/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/json/

[XML](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/xml/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/xml/

## Perbedaan antara JSON, XML, dan HTML

Ada tiga perbedaan yang paling terlihat antara ketiga dokumen ini. yaitu:

1. Konten: informasi sebenarnya yang ingin ditampilkan.
2. Struktur: bagaimana semua informasi dalam dokumen diatur.
3. Formatting: bagaimana dokumen itu ingin dibaca secara visual kepada yang membacanya.

Sebenarnya, XML adalah pengembangan lebih lanjut dari HTML. Sama seperti SGML, HTML akan membungkus konten dalam tag, tetapi tidak seperti itu, aturan tentang tag mana yang dapat digunakan, kapan, dan di mana jauh lebih ketat. Meskipun ini tidak terlalu memengaruhi pemformatan dokumen. itu mempengaruhi struktur informasi dalam dokumen. Pada titik ini kemudahan penggunaan HTML sangat bagus untuk pengembang tetapi kurangnya struktur yang disediakan oleh SGML masih belum ada. Ini mengarah pada pembuatan XML. XML akan mencoba mengatasi masalah ini secara langsung dengan mempertahankan semua aturan ketat SGML, oleh karena itu mempertahankan struktur informasi (seperti halnya database), tanpa mengkhawatirkan pemformatan sama sekali. Jadi disini saya akan fokus pada perbedaan JSON dan XML. <br>

### Apa itu JSON

adalah format file yang menggunakan teks yang dapat dibaca manusia untuk menyimpan dan mentransmisikan objek data yang berisi pasangan atribut-nilai dan array. JSON digunakan untuk menyimpan informasi secara terorganisir dan mudah diakses. JSON adalah singkatan dari JavaScript Object Notation. Ini menawarkan kumpulan data yang dapat dibaca manusia yang dapat diakses secara logis.

### Apa itu XML

adalah bahasa markup yang dapat diperluas yang dirancang untuk menyimpan data. Ini populer digunakan untuk mentransfer data. Ini peka huruf besar-kecil. XML memungkinkan Anda untuk mendefinisikan elemen markup dan menghasilkan bahasa markup yang disesuaikan. Elemen adalah unit dasar dalam bahasa XML. Ekstensi file XML adalah .xml.

### Tabel Perbedaan

|                              JSON                              |                                             XML                                             |
| :------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
|                     JSON object has a type                     |                                    XML data is typeless                                     |
|           JSON types: string, number, array, Boolean           |                                All XML data should be string                                |
|           Data is readily accessible as JSON objects           |                                XML data needs to be parsed.                                 |
|              JSON is supported by most browsers.               |                           Cross-browser XML parsing can be tricky                           |
|               JSON has no display capabilities.                |         XML offers the capability to display data because it is a markup language.          |
|                    Retrieving value is easy                    |                                Retrieving value is difficult                                |
| A fully automated way of deserializing/serializing JavaScript. |         Developers have to write JavaScript code to serialize/de-serialize from XML         |
|                   Native support for object.                   | The object has to be express by conventions – mostly missed use of attributes and elements. |
|                It supports only UTF-8 encoding.                |                                It supports various encoding.                                |
|        JSON files are easy to read as compared to XML.         |             XML documents are relatively more difficult to read and interpret.              |
|        It does not provide any support for namespaces.         |                                   It supports namespaces.                                   |
|                      It is less secured.                       |                                It is more secure than JSON.                                 |

## Data Delivery dalam Pengimplementasian Sebuah Platform

Dalam sebuah aplikasi berbasis platform. kita tidak dapat menyimpan semua data dalam local device saja. Jika itu dilakukan, maka semua data dalam platform tersebut akan menjadi static dan tidak banyak keuntungan dari hal tersebut. Maka dari itu, digunakanlah data delivery yang bertujuan untuk suatu aplikasi melakukan pertukaran data antara clients dan juga server di mana kita menyimpan data dinamis. Maka dari itu digunakan lah metode-metode yang sesuai untuk data delivery tersebut. Metode yang sering digunakan antara lain adalah JSON dan XML. Pada dasarnya, metode ini dapat digunakan untuk mengatur data kompleks dalam format tertentu yang dapat dipahami oleh berbagai bahasa pemrograman dan API, sehingga dapat mempermudah pertukaran data.

## Langkah-Langkah Implementasi

1. Untuk membuat sebuah `django-app` bernama `mywatchlist` masukan perintah `python manage.py startapp mywatchlist` ke terminal pada root directory.
2. Tambahkan `path('mywatchlist/', include('mywatchlist.urls'))` ke `urlpatterns` pada file `/project_django/urls.py`. Kemudian, tambahkan `path('html/', show_mywatchlist_html, name='show_mywatchlist_html')`, `path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml')` , `path('json/', show_mywatchlist_json, name='show_mywatchlist_json')` pada file `/mywatchlist/urls.py`. Penambahan ini dapat disesuaikan dengan fungsi dari views.py yang dibuat.
3. buat model pada `/mywatchlist/models.py` dengan nama dapat disesuaikan (pada kasus ini MyWatchListItem) dan dengan field yang sesuai dengan ketentuan yang ada, yaitu watched, title, rating, release_date, dan review. Setelah itu dilakukan migrasi agar model terbuat pada database.

## Postman Screenshoot

### JSON

![JSON](../static/postman_pbp_tugas_3_json.jpg?raw=true)

### HTML

![HTML](../static/postman_pbp_tugas_3_html.jpg?raw=true)

### XML

![XML](../static/postman_pbp_tugas_3_xml.jpg?raw=true)
