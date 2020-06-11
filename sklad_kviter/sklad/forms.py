from django import forms
from .models import List_details


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

	## Для клааса наверное
	# def __init__(self, *args, **kwargs):
	# 	super(DetailId, self).__init__(*args, **kwargs)
	# 	self.fields['field1'].widget.attrs.update({'class': 'list_del_detil'})

