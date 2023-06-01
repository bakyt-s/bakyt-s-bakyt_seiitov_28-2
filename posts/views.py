from django.shortcuts import render, redirect

from posts.models import Product
from posts.froms import ProductCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id_):
    if request.method == 'GET':
        product = Product.objects.get(id=id_)

        context = {
            'product': product,
            'comments': product.comment_set.all()
        }
        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':

        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                rate=form.cleaned_data.get('rate'),
                article=form.cleaned_data.get('article'),
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                description=form.cleaned_data.get('description')
            )

            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
