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


class List_products_Form(forms.Form):
	class Meta:
		model = List_products
		fields = ['title','count','obj_details']

		widget = {
				'title': forms.TextInput(),
				'count': forms.NumberInput(),
				'obj_details': forms.ChoiceField()

		}