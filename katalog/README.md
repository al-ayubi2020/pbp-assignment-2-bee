## Assignment 2

(isi link heroku disini)

## Bagan
![Bagan](../static/diagram.png?raw=true)<br>
Request diberikan oleh user dalam bentuk URL lalu views akan menangkap request tersebut sesuai dengan route yang ditentukan. setelah diterima oleh views, views akan melakukan query kepada DB melalui file models. lalu, models akan melakukan transaksi dengan DB dan models akan memberikan respons yang sesuai kepada views. Respons diterima oleh views dan views akan mereturn data bertipe dictionary kepada template yang dipilih melalui fungsi render. Dan hasilnya, template akan terender di browser client.
