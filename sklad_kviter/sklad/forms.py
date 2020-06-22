from django import forms
from .models import List_details, Detail_in_products, List_products


class DetailForm(forms.ModelForm):
	class Meta:
		model = List_details
		fields = ['title', 'count', 'slug']

		widgets = {
			'title': forms.TextInput(),
			'count': forms.NumberInput(),
			'slug': forms.TextInput(),
		}


class DetailId(forms.Form):
	field1 = forms.ModelChoiceField(queryset = List_details.objects.all(), empty_label="удалить деталь")
	field1.widget.attrs.update({'class': 'list_del_detil'})


class Detail_in_products_Form(forms.ModelForm):
	class Meta:
		model = Detail_in_products
		fields = ['detail', 'detail_count']

		widget = {
			'detail': forms.Select(),
			'detail_count': forms.NumberInput(),
		}

class Case_delete_Form(forms.Form):
	list_case = forms.ModelChoiceField(queryset = Detail_in_products.objects.all(), empty_label="удалить кейс")
	list_case.widget.attrs.update({'class': 'list_del_detil'})


# для показа и изменения
class List_products_Form(forms.ModelForm):
	class Meta:
		model = List_products
		fields = ['title','count', 'obj_details', 'slug']

		widget = {
				'title': forms.TextInput(),
				'count': forms.NumberInput(),
				'obj_details': forms.ChoiceField(),
				'slug': forms.TextInput(),

		}

	cheek = forms.BooleanField(required=False)

# для создание изделия
class ListProductsForm(forms.ModelForm):
	class Meta:
		model = List_products
		fields = ['title','count','obj_details',]

		widget = {
				'title': forms.TextInput(),
				'count': forms.NumberInput(),
				'obj_details': forms.ChoiceField(),
		}

class Product_delete_Form(forms.Form):
	list_products = forms.ModelChoiceField(queryset = List_products.objects.all(), empty_label="удалить ИЗДЕЛИЕ")
	list_products.widget.attrs.update({'class': 'list_del_detil'})
