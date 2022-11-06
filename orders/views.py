from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from carts.models import CartItem
import datetime
from .models import Order, OrderProduct
from .forms import OrderForm
from product.models import Product
import json

data_1 = []


def place_order(request, total=0, quantity=0):
    current_user = request.user


    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    grand_total = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    grand_total = total


    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            data = Order()
            data.user = current_user
            data.fisrt_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.ip = request.META.get("REMOTE_ADDR")

            data.save()
            print(data)


            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date =d.strftime("%Y%m%d")

            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=request.user, order_number=data.order_number)

            # Перемещение елементов с корзины на такблицу с заказами

            for item in cart_items:
                orderproduct = OrderProduct()
                orderproduct.order_id = order.id
                orderproduct.user_id = request.user.id
                orderproduct.product_id = item.product_id
                orderproduct.quantity = item.quantity
                orderproduct.product_price = item.product.price
                orderproduct.ordered = True
                orderproduct.save()


                cart_item = CartItem.objects.get(id=item.id)
                product_variation = cart_item.variations.all()
                orderproduct = OrderProduct.objects.get(id=orderproduct.id)
                orderproduct.variations.set(product_variation)
                orderproduct.save()

                # уменьшить количество продаваемой продукции

                product = Product.objects.get(id=item.product_id)
                product.stock -= item.quantity
                product.save()

            # очистка корзины
            CartItem.objects.filter(user=request.user).delete()



            return redirect('/')

            # data_2 = {
            #     'order_number': order_number
            # }


            
            # data_1.append(data_2)  


    else:
        return redirect('store')


def order_complete(request):
    order_number_main = request.GET.get('order_number')
    print(order_number_main)

    try:
        order = Order.objects.get(order_number=order_number_main, is_ordered=True)
        print('gechdi')
        ordered_products = OrderProduct.objects.filter(order=order.id)

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number
        }
        return render(request, 'order_complete.html', context)
    except (Order.DoesNotExist):
        print('gechmedi')
        return redirect('home')
        








