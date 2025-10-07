from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Product
from main.forms import ProductForm, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse


@login_required(login_url='/login')
def home_page(request):
    # ambil message yang mungkin ada dari request sebelumnya
    django_messages = []
    for message in messages.get_messages(request):
        django_messages.append({
            "level": message.level,
            "message": message.message,
            "tags": message.tags,
        })

    context = {
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'django_messages': django_messages,  # kirim message ke template
    }
    return render(request, 'home.html', context)


@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            messages.success(
                request, "New product has been added successfully!")
            return redirect('main:home_page')

        context = {'form': form}

        return render(request, "create_product.html", context)

    elif request.method == "GET":
        context = {'form': form}
        return render(request, "create_product.html", context)

    return HttpResponse(status=404)


@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        messages.error(
            request, "Access denied. You are not the owner of this product.")
        return redirect('main:home_page')
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, "Product updated successfully!")
        return redirect('main:home_page')
    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)


@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        messages.error(
            request, "Access denied. You are not the owner of this product.")
        return redirect('main:home_page')
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return HttpResponseRedirect(reverse('main:home_page'))
    context = {'product': product}
    return render(request, 'delete_product.html', context)


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)


@login_required(login_url='/login')
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


# kudu nambahin filter, butuh buat call di javascript
@login_required(login_url='/login')
def show_json(request):
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'my':
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()
    return HttpResponse(serializers.serialize("json", product_list), content_type="application/json")


@login_required(login_url='/login')
def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


# kudu tambahin format data sendiri biar bsa include seller_name di jsonnya
@login_required(login_url='/login')
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            "pk": product.pk,
            "fields": {
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "description": product.description,
                "thumbnail": product.thumbnail,
                "category": product.category,
                "is_featured": product.is_featured,
                "seller_name": product.user.username if product.user else "[Anonymous]"
            }
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."}, status=404)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Registration successful! You will be redirected to the login page."
            }, status=201)
        else:
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field.capitalize()}: {error}")
            return JsonResponse({
                "status": "error",
                "message": "Registration failed. Please correct the errors below.",
                "errors": error_messages
            }, status=400)
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {
                    "status": "success",
                    "message": "Login successful!",
                    "redirect_url": reverse("main:home_page")
                }
                response = JsonResponse(response_data, status=200)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid username or password."
                }, status=401)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Please fill out all fields correctly."
            }, status=400)
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                "status": "success",
                "message": "New product has been added successfully!"
            }, status=201)
        else:
            return JsonResponse({
                "status": "error",
                "message": "There was an error with your input. Please check the form again.",
                "errors": form.errors
            }, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)


@login_required(login_url='/login')
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Access denied."}, status=403)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully!"}, status=200)
        else:
            return JsonResponse({"status": "error", "message": "Invalid data.", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)


@login_required(login_url='/login')
def delete_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Access denied."}, status=403)
        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully!"}, status=200)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)
