from django.shortcuts import render, redirect
from .models import *
from .forms import QuestionForm, UserReg
from datetime import datetime
from django.http import JsonResponse
import json


def index(request):
    items = Item.objects.all()

    form = QuestionForm(request.POST)

    if form.is_valid():
        question = form.save(commit=False)
        question.date = datetime.now()
        question.save()

        form.save_m2m()

        return redirect('success')
    else:
        form = QuestionForm()

    return render(request, "main/index.html", {"items": items, "form": form})

def success_form(request):
    return render(request, "main/successform.html")


def shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    return render(request, "main/cart.html", {"items": items})


def checkout(request):
    return render(request, "main/Checkout.html")


def item(request, code):
    item = Item.objects.get(code=code)
    return render(request, 'main/item.html', {'item': item})

def registry(request):

    if request.method == "POST":
        form = UserReg(request.POST)

        if form.is_valid():
            customer = Customer()
            customer.user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            customer.name = form.cleaned_data['name']
            customer.email = form.cleaned_data['email']
            customer.phone_number = form.cleaned_data['phone_number']
            customer.gender = form.cleaned_data['gender']

            customer.save()

            return redirect('login')
    else:
        form = UserReg()

    return render(request, 'registration/registration.html', {'form':form})


def profile(request):
    return render(request, 'main/profile.html')


def updateItem(request):
    data = json.loads(request.body)
    itemCode = data['itemCode']
    action = data['action']

    customer = request.user.customer
    item = Item.objects.get(code=itemCode)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

