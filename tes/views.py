from django.shortcuts import redirect, render
from django.db import connections
from django.contrib import messages
from tes.models import Produk, Kategori, Status
# from tes.forms import tambahProduk

# Create your views here.
cursor = connections['default'].cursor()
def dashboard(request):
    if request.GET.get('filter'):
        filter_status = request.GET.get('filter')
        print( filter_status)
        if filter_status == "Yes":
            product = Produk.objects.raw("SELECT id_product, produk.id_product AS 'id_produk',produk.nama_produk AS 'nama_produk',produk.harga as 'harga' , kategori.nama_kategori as 'kategori', status.nama_status as 'status' FROM produk JOIN kategori ON kategori.id_kategori = kategori_id JOIN status ON status.id_status = status_id WHERE status.nama_status = 'bisa dijual'")
        else:
            product = Produk.objects.raw("SELECT id_product, produk.id_product AS 'id_produk',produk.nama_produk AS 'nama_produk',produk.harga as 'harga' , kategori.nama_kategori as 'kategori', status.nama_status as 'status' FROM produk JOIN kategori ON kategori.id_kategori = kategori_id JOIN status ON status.id_status = status_id")        
    else:
        product = Produk.objects.raw("SELECT id_product, produk.id_product AS 'id_produk',produk.nama_produk AS 'nama_produk',produk.harga as 'harga' , kategori.nama_kategori as 'kategori', status.nama_status as 'status' FROM produk JOIN kategori ON kategori.id_kategori = kategori_id JOIN status ON status.id_status = status_id")
    return render(request,"dashboard.html",{'raw_produk': product})

def tambahProduct(request):
    if request.POST:
        nama_produk = request.POST.get("nama_produk")
        harga = request.POST.get("harga")
        kategori_id = request.POST.get("kategori")
        status_id = request.POST.get("status")
        cursor.execute("INSERT INTO produk (id_product, nama_produk, harga, kategori_id, status_id) VALUES (NULL, \'{}\', {}, {}, {})".format(nama_produk,harga,kategori_id,status_id))
        listKategori = Kategori.objects.raw("SELECT * from kategori")
        listStatus = Status.objects.raw("SELECT * from status")
        data = {
            "kategori":listKategori,
            "status":listStatus,
            "pesan":"Produk berhasil ditambahkan"
        }
        return render(request, "tambah_produk.html", data)
    else:
        listKategori = Kategori.objects.raw("SELECT * from kategori")
        listStatus = Status.objects.raw("SELECT * from status")
        data = {
            "kategori":listKategori,
            "status":listStatus
        }
        return render(request, "tambah_produk.html", data)

def hapusProduct(request, id_produk):
    cursor.execute("DELETE FROM produk WHERE produk.id_product = {}".format(id_produk))
    messages.success(request, "Produk berhasil dihapus")
    return redirect("dashboard")

def editProduct(request, id_produk):
    if request.POST:
        product_id = request.POST.get("idProduk")
        nama_produk = request.POST.get("nama_produk")
        harga = request.POST.get("harga")
        kategori_id = request.POST.get("kategori")
        status_id = request.POST.get("status")
        cursor.execute("UPDATE produk SET nama_produk = \'{}\', harga = {}, kategori_id = {}, status_id = {} WHERE produk.id_product = {}".format(nama_produk,harga,kategori_id,status_id,id_produk ))
        messages.success(request, "Produk berhasil diupdate")
        return redirect("dashboard")

    else:
        product = Produk.objects.raw("SELECT id_product, produk.id_product AS 'id_produk',produk.nama_produk AS 'nama_produk',produk.harga as 'harga' , kategori.nama_kategori as 'kategori', status.nama_status as 'status' FROM produk JOIN kategori ON kategori.id_kategori = kategori_id JOIN status ON status.id_status = status_id WHERE produk.id_product = {}".format(id_produk))
        listKategori = Kategori.objects.raw("SELECT * from kategori")
        listStatus = Status.objects.raw("SELECT * from status")
        data = {
            "id":id_produk,
            "raw_produk":product,
            "kategori":listKategori,
            "status":listStatus
        }
        # print(id_produk)
        return render(request,"edit_produk.html",data)