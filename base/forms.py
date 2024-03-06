from django import forms
from .models import ProductCategory
from .models import Product
from .models import BillItem, Bill

class CategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ['name','del_flag']
        exclude = ("created_at","created_by")


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name','category_id','rate']
        exclude = ("created_at","created_by")

class BillItemForm(forms.ModelForm):

    class Meta:
        model = BillItem
        fields = ['product_id','product_name','qty','rate','total',]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].required = False
        self.fields['product_id'].required = False
        self.fields['qty'].required = False
        self.fields['total'].required = False

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name','total_amount','product_ids']
        exclude = ("created_by",)
        widgets = {
            'product_ids': forms.CheckboxSelectMultiple,
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = False
            self.fields['total_amount'].required = False
            self.fields['product_ids'].required = False
            self.fields['created_at'].required = False
            self.fields['created_by'].required = False

