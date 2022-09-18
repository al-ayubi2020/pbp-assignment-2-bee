## Assignment 3

[HTML](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/html/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/html/

[JSON](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/json/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/json/

[XML](https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/xml/), atau https://pbp-assignment-2-bee.herokuapp.com/mywatchlist/xml/

## Perbedaan antara JSON, XML, dan HTML!

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
