from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
from store.views import product_all

@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.','')
    total = int(total)
    if request.method == "POST":
            message_email = request.POST['message-email']
            customer_name = request.POST['customer_name']
            address = request.POST['address']
            address2 = request.POST['address2']
            Country = request.POST['Country']
            State = request.POST['State']
            Postcode = request.POST['Postcode']



            send_mail(
                'Sender',
                'message from ' + customer_name + ','
                 + message_email + '.'
                  + "My address" + Country+ ',' +address+',' + address2+"."
                + 'State: ' + State + ". Postcode" + Postcode,
                
                message_email,
                ['nsanbaev.15@gmail.com']
            )
            return redirect("account:dashboard")

    else:
        return render(request,'payment/home.html')
    

