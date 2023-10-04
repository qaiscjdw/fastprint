from django.forms import ModelForm
from tes.models import Produk


class tambahProduk(ModelForm):
    class Meta:
        model = Produk
        fields = "__all__"
