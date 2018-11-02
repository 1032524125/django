from django import forms


class GoodsDetailForm(forms.Form):
    name = forms.CharField(required=True)
    goods_sn = forms.CharField(required=True)
    category = forms.CharField(required=True)
    goods_nums = forms.CharField(required=True)
    market_price = forms.CharField(required=True)
    shop_price = forms.CharField(required=True)
    goods_brief = forms.CharField(required=True)



