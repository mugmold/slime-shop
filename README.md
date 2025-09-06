### Repo: https://github.com/mugmold/slime-shop
### Web: https://bermulya-anugrah-slimeshop.pbp.cs.ui.ac.id

---

# "Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)."

### 1. Membuat project Django baru
Pertama saya membuat sebuah project Django bernama slime_shop dengan perintah ```django-admin startproject slime_shop.```

Setelah project utama selesai dibuat, saya menambahkan sebuah app baru bernama main dengan perintah ```python manage.py startapp main.```

### 2. Setup environment & project awal
Saya membuat file ```.env``` dan ```.env.prod``` untuk menyimpan variable penting (misalnya konfigurasi database).

Saya juga membuat file ```requirements.txt``` untuk setup dependencies agar nantinya bisa dikelola dan digunakan dengan baik serta mudah di-install di environment lain.

Saya juga menambahkan file ```.gitignore``` agar file yang tidak penting (seperti cache, migrations, dll.) tidak ikut di push ke repository.

### 3. Konfigurasi settings.py
Saya mengedit ```settings.py``` pada project ```slime_shop``` untuk mengatur konfigurasi database sesuai dengan arahan tutorial sebelumnya (edit database, tambahkan variable ```PRODUCTION```, dll.).

Pada tahap akhir, setelah deploy ke ```PWS```, saya juga menambahkan domain ```PWS``` ke dalam ```ALLOWED_HOSTS``` agar aplikasi bisa di host di pws, dan juga bisa diakses oleh publik.

### 4. Setup URL
Pada ```slime_shop/urls.py```, saya menambahkan route agar bisa terhubung dengan app main.

Di dalam ```main/urls.py```, saya mendefinisikan path yang menghubungkan URL ke fungsi ```home_page```. Dari sini juga saya sambungkan dengan template HTML (ex: ```home.html```) untuk menampilkan frontend.

### 5. Membuat view dan template
Pada ```main/views.py```, saya membuat fungsi ```home_page``` untuk menampilkan home page awal.

Home page tersebut berisi nama toko saya, serta informasi identitas pribadi (nama dan kelas).

Fungsi ```home_page``` ini kemudian dihubungkan ke template HTML (```home.html```) yang sudah saya buat.

### 6. Membuat model
Pada ```main/models.py```, saya membuat sebuah model Django bernama Product, yang memiliki atribut yang sesuai dengan kebutuhan Tugas1 dan menambahkan atribut ```stock``` untuk menampilkan stock product saat ini, serta juga menambahkan sedikit validator untuk ```price``` dan ```stock``` agar tidak memiliki value negatif.

Model ini kemudian akan digunakan untuk mengelola data yang tersimpan di database.

### 7. Setup Git dan Deploy ke PWS
Saya inisialisasi Git repository, lalu push project ke ```PWS```.

Setelah itu saya deploy aplikasi ke ```GitHub```.

Setelah memastikan aplikasi berhasil jalan, saya melakukan penyesuaian terakhir pada ```settings.py``` (menambahkan ```ALLOWED_HOSTS```), lalu push ulang ke ```GitHub``` dan ```PWS``` agar update-nya ter-deploy.

### 8. Membuat README.md
Terakhir, saya membuat file ```README.md``` yang berisi dokumentasi proyek, termasuk link menuju repository ```GitHub``` dan link aplikasi ```PWS```, serta jawaban dari pertanyaan yang diberikan.

Setelah selesai, saya push ulang project agar ```README.md``` ikut tersimpan di repository.

---

# "Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas ```html```."

![Django R-R Model](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1619466042369%2Fb3LAaF7TO.png)

### alur request–response pada web aplikasi Django (secara sederhana, sesuai pemahaman saya):
### 1. Client (Browser/User)
-> mengirim request, misalnya mengetik URL ```https://bermulya-anugrah-slimeshop.pbp.cs.ui.ac.id``` di web browser

### 2. ```urls.py``` (URL Dispatcher)
-> Django menerima request serta mengecek pola URL dgn yang ada di file ```urls.py``` untuk mencari kecocokan

### 3. ```views.py``` (View Function/Class)
-> fungsi view yang sesuai akan dijalankan. View bisa memproses data request, memanggil model, atau langsung menyiapkan response yang nantinya akan diberikan kepada user

### 4. ```models.py``` (Database model)
-> jika view butuh data dari database, maka view akan memanggil database model untuk query/insert/update data

### 5. Template HTML (frontend)
-> view kemudian merender data ke dalam file HTML menggunakan template engine Django
(```Note```: Asumsi disini adalah server mengirimkan response berupa ```HTML```)

### 6. Response ke Client
-> HTML serta data tambahan yang sudah jadi dikirim kembali ke browser untuk ditampilkan ke user

---

# "Jelaskan peran ```settings.py``` dalam proyek Django!"

```settings.py``` berperan sebagai pusat konfigurasi proyek Django. File ini menyimpan semua pengaturan penting seperti konfigurasi database, daftar aplikasi yang digunakan,, template, pengaturan keamanan (secret key, debug mode), daftar host yang diizinkan, dll. Dengan adanya ```settings.py```, semua aspek proyek bisa diatur secara terpusat sehingga mudah dikelola dan disesuaikan dengan environment yang ada.

---

# "Bagaimana cara kerja migrasi database di Django?"

Migrasi di Django adalah mekanisme untuk menerapkan perubahan pada model ke dalam database secara otomatis. Prosesnya bekerja dalam dua tahap utama:

1. Saat kita menjalankan ```python manage.py makemigrations```, Django membaca perubahan yang ada di ```models.py``` dan membuat file migrasi (semacam blueprint perubahan database).
2. Lalu dengan ```python manage.py migrate```, Django mengeksekusi file migrasi tersebut ke database, misalnya membuat tabel baru, menambah kolom, atau mengubah struktur tabel.

---

# "Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?"

Django sering dijadikan framework pertama dalam pembelajaran pengembangan perangkat lunak karena sifatnya yang ```“batteries included”```, yang artinya sudah menyediakan banyak fitur bawaan seperti autentikasi user, sistem admin, ORM untuk menghubungkan aplikasi dengan database, serta struktur proyek yang rapi dan terstandarisasi. Hal ini membuat pemula tidak perlu membangun semuanya dari nol, sehingga bisa lebih cepat membuat aplikasi web dengan mudah. Selain itu, dokumentasinya lengkap, komunitasnya besar, dan banyak digunakan di industri nyata, sehingga belajar Django tidak hanya mempermudah pemahaman dasar konsep web development, tetapi juga relevan untuk kebutuhan professional.

---

# "Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?"

Untuk tutorial 1, saya tidak memiliki saran khusus karena menurut saya semua sudah disampaikan dengan baik dan jelas. Penjelasan serta arahan yang diberikan sudah sangat membantu dalam memahami materi, sehingga tidak ada saya tidak memiliki kritik/saran yang dapat disampaikan.