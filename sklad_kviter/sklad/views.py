from django.shortcuts import render

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import List_details, Detail_in_products
from .forms import DetailForm, DetailId, Detail_in_products_Form


class Sklad_list(LoginRequiredMixin, View):

	def get(self, request):

		form = DetailForm()
		formid = DetailId()
		form_case = Detail_in_products_Form()

		details = List_details.objects.all()
		forms = []
		for i in details:
			forms.append(DetailForm(instance=i))

		context = {
			'form': form,
			'forms': forms,
			'formid': formid,
			'form_case': form_case,
		}	

		return render(request, 'sklad/sklad_list.html', context=context)


	def post(self, request):

		details = List_details.objects.all()
		forms = []
		for i in details:
			forms.append(DetailForm(instance=i))

		if request.POST.get('detail_button_plus'):

			slug = request.POST['detail_button_plus']
			detail = List_details.objects.get(slug__iexact=slug)
			bound_form = DetailForm(request.POST, instance=detail)
			if bound_form.is_valid():
				bound_form.save()
			else:
				return render(request, 'sklad/sklad_list.html', context={"form_errors": bound_form, 'forms': forms,})

			name_detal = request.POST['detail_button_plus']
			obj_detal = List_details.objects.get(slug__iexact=name_detal)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			obj_detal.count = str(int(obj_detal.count) + int(number))
			obj_detal.save()

			return redirect('/sklad')

		elif request.POST.get('detail_button_minus'):
			
			slug = request.POST['detail_button_minus']
			detail = List_details.objects.get(slug__iexact=slug)
			bound_form = DetailForm(request.POST, instance=detail)
			if bound_form.is_valid():
				bound_form.save()
			else:
				return render(request, 'sklad/sklad_list.html', context={"form_errors": bound_form, 'forms': forms,})

			name_detal = request.POST['detail_button_minus']
			obj_detal = List_details.objects.get(slug__iexact=name_detal)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			obj_detal.count = str(int(obj_detal.count) - int(number))
			obj_detal.save()

			return redirect('/sklad')

		elif request.POST.get('detail_create'):

			title = request.POST.get('title')
			count = request.POST.get('count')

			obj = List_details(title = title, count = count)
			obj.save()

			return redirect('/sklad')

		elif request.POST.get('detail_case'):
			print("------------------")
			print(request)
			print("------------------")
			print(request.POST)
			print("------------------")
			bound_form = Detail_in_products_Form(request.POST)

			all_obj_case = Detail_in_products.objects.all()
			print('_____________________')
			print(all_obj_case)
			print('______________________')

			if bound_form.is_valid():
				new_case = bound_form.save()
			all_obj_case = Detail_in_products.objects.all()
			print('_____________________')
			print(all_obj_case)
			print('______________________')
			return redirect('/sklad')



		elif request.POST.get('detail_delete'):

			id = request.POST['field1']
			obj = List_details.objects.get(id = id)
			obj.delete()

			return redirect('/sklad')

