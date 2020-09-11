from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import List_details, Detail_in_products, List_products
from .forms import DetailForm, DetailId, Detail_in_products_Form, Case_delete_Form, List_products_Form, Product_delete_Form, ListProductsForm, Calculation_product_form


class Sklad_list(LoginRequiredMixin, View):

	def get(self, request):

		form = DetailForm()
		formid = DetailId()
		product_create = List_products_Form()
		product_del = Product_delete_Form()

		product = List_products.objects.all()
		form_product = []
		for i in product:
			form_product.append(List_products_Form(instance=i))

		details = List_details.objects.all()
		forms = []
		for i in details:
			forms.append(DetailForm(instance=i))

		context = {
			'form': form,
			'forms': forms,
			'formid': formid,
			'product_create': product_create,
			'form_product': form_product,
			'product_del': product_del,
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

		elif request.POST.get('detail_delete'):

			id = request.POST['field1']
			obj = List_details.objects.get(id = id)
			obj.delete()

			return redirect('/sklad')

		elif request.POST.get('product_delete'):

			id = request.POST['list_products']
			obj = List_products.objects.get(id = id)
			obj.delete()

			return redirect('/sklad')

		if request.POST.get('product_button_plus'):

			slug = request.POST['product_button_plus']
			product = List_products.objects.get(slug__iexact=slug)
			bound_form = List_products_Form(request.POST, instance=product)

			if bound_form.is_valid():
				bound_form.save()

			slug_product = request.POST['product_button_plus']
			obj_product = List_products.objects.get(slug__iexact=slug_product)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			if 'cheek' in request.POST:
				l = list(obj_product.obj_details.values('detail_id', 'detail_count'))
				for i in l:
					z = list(i.values())
					d = List_details.objects.get(id=z[0])
					d.count = int(d.count) - (int(z[1])*int(number))
					d.save()
			obj_product.count = int(obj_product.count) + int(number)
			obj_product.save()

			return redirect('/sklad')

		elif request.POST.get('product_button_minus'):
			
			slug = request.POST['product_button_minus']
			product = List_products.objects.get(slug__iexact=slug)
			bound_form = List_products_Form(request.POST, instance=product)
			if bound_form.is_valid():
				bound_form.save()

			slug_product = request.POST['product_button_minus']
			obj_product = List_products.objects.get(slug__iexact=slug_product)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			if 'cheek' in request.POST:
				l = list(obj_product.obj_details.values('detail_id', 'detail_count'))
				for i in l:
					z = list(i.values())
					d = List_details.objects.get(id=z[0])
					d.count = int(d.count) + (int(z[1])*int(number))
					d.save()

			obj_product.count = int(obj_product.count) - int(number)
			obj_product.save()

			return redirect('/sklad')





class Product_create(LoginRequiredMixin, View):

	def get(self, request):

		form_case = Detail_in_products_Form()
		case_del_form = Case_delete_Form()
		product_create = List_products_Form()

		context = {
			'form_case': form_case,
			'case_del_form': case_del_form,
			'product_create': product_create,
		}	

		return render(request, 'sklad/product_create.html', context=context)

	def post(self, request):

		if request.POST.get('product_create'):

			bound_form = ListProductsForm(request.POST)

			if bound_form.is_valid():
				b = bound_form.save()

			return redirect('/sklad')

		elif request.POST.get('detail_case'):

			bound_form = Detail_in_products_Form(request.POST)

			if bound_form.is_valid():
				new_case = bound_form.save()

			return redirect('/sklad/product_create')

		elif request.POST.get('case_delete'):

			id = request.POST['list_case']
			obj = Detail_in_products.objects.get(id = id)
			obj.delete()

			return redirect('/sklad/product_create')


class Product_update(LoginRequiredMixin, View):

	def get(self, request, slug):

		product = List_products.objects.get(slug__iexact=slug)
		form_product = List_products_Form(instance=product)
		form_case = Detail_in_products_Form()
		case_del_form = Case_delete_Form()

		context = {
		'product': product,
		'form_product': form_product,
		'form_case': form_case,
		'case_del_form': case_del_form,
		}

		return render(request, 'sklad/product_update.html', context=context)

	def post(self, request, slug):

		if request.POST.get('product_button_plus'):

			slug = request.POST['product_button_plus']
			product = List_products.objects.get(slug__iexact=slug)
			bound_form = List_products_Form(request.POST, instance=product)

			if bound_form.is_valid():
				bound_form.save()

			slug_product = request.POST['product_button_plus']
			obj_product = List_products.objects.get(slug__iexact=slug_product)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			if 'cheek' in request.POST:
				l = list(obj_product.obj_details.values('detail_id', 'detail_count'))
				for i in l:
					z = list(i.values())
					d = List_details.objects.get(id=z[0])
					d.count = int(d.count) - (int(z[1])*int(number))
					d.save()
			obj_product.count = int(obj_product.count) + int(number)
			obj_product.save()

			product = List_products.objects.get(slug__iexact=slug)
			form_product = List_products_Form(instance=product)
			form_case = Detail_in_products_Form()
			case_del_form = Case_delete_Form()
			context = {
			'product': product,
			'form_product': form_product,
			'form_case': form_case,
			'case_del_form': case_del_form,
			}
			return render(request, 'sklad/product_update.html', context=context)

		elif request.POST.get('product_button_minus'):
			
			slug = request.POST['product_button_minus']
			product = List_products.objects.get(slug__iexact=slug)
			bound_form = List_products_Form(request.POST, instance=product)
			if bound_form.is_valid():
				bound_form.save()

			slug_product = request.POST['product_button_minus']
			obj_product = List_products.objects.get(slug__iexact=slug_product)
			number = request.POST['number']
			if request.POST['number'] == '':
				number = 0
			if 'cheek' in request.POST:
				l = list(obj_product.obj_details.values('detail_id', 'detail_count'))
				for i in l:
					z = list(i.values())
					d = List_details.objects.get(id=z[0])
					d.count = int(d.count) + (int(z[1])*int(number))
					d.save()

			obj_product.count = int(obj_product.count) - int(number)
			obj_product.save()

			product = List_products.objects.get(slug__iexact=slug)
			form_product = List_products_Form(instance=product)
			form_case = Detail_in_products_Form()
			case_del_form = Case_delete_Form()
			context = {
			'product': product,
			'form_product': form_product,
			'form_case': form_case,
			'case_del_form': case_del_form,
			}
			return render(request, 'sklad/product_update.html', context=context)
		
		elif request.POST.get('detail_case'):

			bound_form = Detail_in_products_Form(request.POST)

			if bound_form.is_valid():
				new_case = bound_form.save()

			product = List_products.objects.get(slug__iexact=slug)
			form_product = List_products_Form(instance=product)
			form_case = Detail_in_products_Form()
			case_del_form = Case_delete_Form()
			context = {
			'product': product,
			'form_product': form_product,
			'form_case': form_case,
			'case_del_form': case_del_form,
			}

			return render(request, 'sklad/product_update.html', context=context)

		elif request.POST.get('case_delete'):

			id = request.POST['list_case']
			obj = Detail_in_products.objects.get(id = id)
			obj.delete()

			product = List_products.objects.get(slug__iexact=slug)
			form_product = List_products_Form(instance=product)
			form_case = Detail_in_products_Form()
			case_del_form = Case_delete_Form()
			context = {
			'product': product,
			'form_product': form_product,
			'form_case': form_case,
			'case_del_form': case_del_form,
			}

			return render(request, 'sklad/product_update.html', context=context)


class Calculation(LoginRequiredMixin, View):

	def get(self, request):

		form = Calculation_product_form()

		context = {
		'form' : form,
		}
		return render(request, 'calculation/calculation.html', context=context)

	def post(self, request):
		
		if request.POST.get('calculation'):

			id_product = request.POST['product']
			product = List_products.objects.get(id = id_product)
			count = request.POST['count']

			
			l = list(product.obj_details.values('detail_id', 'detail_count'))
			
			details = []
			sum_detail = []
			sum_res_detail = []
			for i in l:
				z = list(i.values())
				# индифицируем деталь
				
				detail = List_details.objects.get(id = z[0])
				details.append(detail)

				sum_d = int(z[1]) * int(count)
				sum_detail.append(sum_d)

				sum_res_d = detail.count - sum_d
				sum_res_detail.append(sum_res_d)

			form = Calculation_product_form()

			context = {
			'form' : form,
			'details':details,
			'sum_detail':sum_detail,
			'sum_res_detail':sum_res_detail,
			}

			return render(request, 'calculation/calculation.html', context=context)
