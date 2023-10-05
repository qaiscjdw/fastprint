# **Documentation**
##### dokumentasi untuk program tes backend programmer di Fastprint
##### Video tes program ini diupload di [Youtube](https://youtu.be/ukXaaESyJ6M)
* Clone repository
```bash
   git clone https://github.com/qaiscjdw/fastprint.git
   cd fastprint
```
* Install library yang akan digunakan
```bash
  pip install -r requirements.txt 
```

* Make migrations dan migrate
```bash
  python manage.py makemigrations && manage.py migrate
```

* Jalankan setup.py
###### Untuk menyimpan data dari api ke database ######
```bash
  python setup.py
```

* Jalankan server
```bash
  python manage.py runserver
```
---
# **Penjelasan Code**
### [Folder fastprint](https://github.com/qaiscjdw/fastprint/tree/main/fastprint)
* Berisi file-file yang digenerate saat membuat project django
* Untuk mengatur database yang defaultnya menggunakan sqlite menjadi mysql perlu diganti bagian [setting.py](https://github.com/qaiscjdw/fastprint/blob/main/fastprint/settings.py)

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'db_testfastprint',
    'USER' : 'root',
    'PASSWORD' : '',
    'HOST' : 'localhost',
    'PORT' : '3306',
    'OPTIONS':{
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
}
```
* Menambahkan apps yang dibuat kedalam [setting.py](https://github.com/qaiscjdw/fastprint/blob/main/fastprint/settings.py)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tes',
]
```
* Menambahkan directory template yang akan digunakan didalam [setting.py](https://github.com/qaiscjdw/fastprint/blob/main/fastprint/settings.py)
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
* Pada file [urls.py](https://github.com/qaiscjdw/fastprint/blob/main/fastprint/urls.py) path sebagai berikut
```python
from django.contrib import admin
from django.urls import path
from tes.views import dashboard,tambahProduct,hapusProduct,editProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard,name="dashboard"),
    path('tambah/',tambahProduct,name="tambah"),
    path('hapus/<int:id_produk>',hapusProduct,name="hapus"),
    path('edit/<int:id_produk>',editProduct,name="edit"),
    
]
```

### [Folder tes](https://github.com/qaiscjdw/fastprint/tree/main/tes)
* Merupakan folder apps yang telah dibuat
* Menambahkan table database yang akan dibuat didalam [models.py](https://github.com/qaiscjdw/fastprint/blob/main/tes/models.py)
```python
class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori'
        
class Produk(models.Model):
    id_product = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255, blank=True, null=True)
    harga = models.IntegerField(blank=True, null=True)
    kategori_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'produk'


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'status'
```
* [views.py](https://github.com/qaiscjdw/fastprint/blob/main/tes/views.py) digunakan untuk mengatur segala action yang ada di web sekaligus tempat raw query sql
  
### [Folder root](https://github.com/qaiscjdw/fastprint/tree/main)
* [manage.py](https://github.com/qaiscjdw/fastprint/blob/main/manage.py) merupakan sebuah file yang digunakan untuk mengatur projek
* [setting.py](https://github.com/qaiscjdw/fastprint/blob/main/setup.py) digunakan untuk mengambil data dari api yang diberikan kedalam database
* [requirement.txt](https://github.com/qaiscjdw/fastprint/blob/main/requirement.txt) adalah tempat seluruh library yang digunakan dalam projek untuk diinstall
