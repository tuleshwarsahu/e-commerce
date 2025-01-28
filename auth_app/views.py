from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Product  # Import Product model
from django.http import JsonResponse , HttpResponse
from datetime import datetime
from django.utils.html import format_html
from django.db.models import Q
from .forms import ProductFilterForm

def home(request):
    dest1 = Product()
    dest1.title = 'Wireless Headphones'
    dest1.price = 99
    dest1.description = 'High-quality wireless headphones with noise cancellation.'
    dest1.category = 'Electronics'
    dest1.image = 'headphone.jpg'
    dest1.sold = True
    dest1.is_sale = True
    dest1.date_of_sale = '2024-11-20'
    
    dest2 = Product()
    dest2.title = 'Gaming Laptop'
    dest2.price = 999
    dest2.description = 'High-quality wireless headphones with noise cancellation.'
    dest2.category = 'Electronics'
    dest2.image = 'gaminglaptop.jpg'
    dest2.sold = False
    dest2.is_sale = False
    dest2.date_of_sale = None
    
    dest3 = Product()
    dest3.title = 'Yoga Mat'
    dest3.price = 299
    dest3.description = 'High-quality wireless headphones with noise cancellation.'
    dest3.category = 'Fitness'
    dest3.image = 'yogamat.jpg'
    dest3.sold = False
    dest3.is_sale = False
    dest3.date_of_sale = None
    
    dest4 = Product()
    dest4.title = 'Smart Watch'
    dest4.price = 499
    dest4.description = 'High-quality wireless headphones with noise cancellation.'
    dest4.category = 'Electronics'
    dest4.image = 'smartwatch.jpg'
    dest4.sold = False
    dest4.is_sale = True
    dest4.date_of_sale = None
    
    dest5 = Product()
    dest5.title = 'Running Shoes'
    dest5.price = 80
    dest5.description = 'Comfortable running shoes for all terrains.'
    dest5.category = 'Fitness'
    dest5.image = 'runningshoes.png'
    dest5.sold = False
    dest5.is_sale = True
    dest5.date_of_sale = None

    dest6 = Product()
    dest6.title = 'Bluetooth Speaker'
    dest6.price = 45
    dest6.description = 'Portable Bluetooth speaker with deep bass.'
    dest6.category = 'Electronics'
    dest6.image = 'bluetoothspeaker.jpg'
    dest6.sold = True
    dest6.is_sale = True
    dest6.date_of_sale = '2024-11-10'

    dest7 = Product()
    dest7.title = 'Office Chair'
    dest7.price = 120
    dest7.description = 'Ergonomic office chair with adjustable height.'
    dest7.category = 'Furniture'
    dest7.image = 'officechair.jpg'
    dest7.sold = False
    dest7.is_sale = False
    dest7.date_of_sale = None

    dest8 = Product()
    dest8.title = 'Standing Desk'
    dest8.price = 300
    dest8.description = 'Adjustable standing desk for a healthy workspace.'
    dest8.category = 'Furniture'
    dest8.image = 'standingdesk.png'
    dest8.sold = True
    dest8.is_sale = False
    dest8.date_of_sale = '2024-11-22'

    dest9 = Product()
    dest9.title = 'Cookware Set'
    dest9.price = 75
    dest9.description = 'Non-stick cookware set for everyday cooking.'
    dest9.category = 'Kitchen'
    dest9.image = 'cookware.jpg'
    dest9.sold = False
    dest9.is_sale = True
    dest9.date_of_sale = None

    dest10 = Product()
    dest10.title = 'Electric Kettle'
    dest10.price = 40
    dest10.description = 'Quick-boil electric kettle with auto shut-off.'
    dest10.category = 'Kitchen'
    dest10.image = 'kettle.jpg'
    dest10.sold = True
    dest10.is_sale = True
    dest10.date_of_sale = '2024-11-05'

    dest11 = Product()
    dest11.title = 'Mountain Bike'
    dest11.price = 500
    dest11.description = 'Durable mountain bike for off-road adventures.'
    dest11.category = 'Fitness'
    dest11.image = 'mountainbike.jpg'
    dest11.sold = False
    dest11.is_sale = False
    dest11.date_of_sale = None

    dest12 = Product()
    dest12.title = 'Winter Jacket'
    dest12.price = 90
    dest12.description = 'Waterproof winter jacket with hood.'
    dest12.category = 'Clothing'
    dest12.image = 'winterjacket.png'
    dest12.sold = True
    dest12.is_sale = True
    dest12.date_of_sale = '2024-11-15'

    dest13 = Product()
    dest13.title = 'Gaming Mouse'
    dest13.price = 35
    dest13.description = 'Ergonomic gaming mouse with RGB lighting.'
    dest13.category = 'Electronics'
    dest13.image = 'gamingmouse.jpg'
    dest13.sold = True
    dest13.is_sale = True
    dest13.date_of_sale = '2024-11-12'

    dest14 = Product()
    dest14.title = 'Leather Wallet'
    dest14.price = 25
    dest14.description = 'Premium leather wallet with RFID protection.'
    dest14.category = 'Accessories'
    dest14.image = 'leatherwallet.png'
    dest14.sold = False
    dest14.is_sale = False
    dest14.date_of_sale = None

    dest15 = Product()
    dest15.title = 'Sunglasses'
    dest15.price = 50
    dest15.description = 'Stylish sunglasses with UV protection.'
    dest15.category = 'Accessories'
    dest15.image = 'sunglasses.png'
    dest15.sold = True
    dest15.is_sale = False
    dest15.date_of_sale = '2024-11-20'

    dest16 = Product()
    dest16.title = 'Microwave Oven'
    dest16.price = 250
    dest16.description = 'High-power microwave oven with digital display.'
    dest16.category = 'Kitchen'
    dest16.image = 'microwaveoven.png'
    dest16.sold = False
    dest16.is_sale = True
    dest16.date_of_sale = None

    dest17 = Product()
    dest17.title = 'Travel Backpack'
    dest17.price = 60
    dest17.description = 'Lightweight travel backpack with multiple compartments.'
    dest17.category = 'Accessories'
    dest17.image = 'bagpack.jpg'
    dest17.sold = True
    dest17.is_sale = True
    dest17.date_of_sale = '2024-11-08'

    dest18 = Product()
    dest18.title = 'Desk Lamp'
    dest18.price = 30
    dest18.description = 'LED desk lamp with adjustable brightness.'
    dest18.category = 'Furniture'
    dest18.image = 'desklamp.jpg'
    dest18.sold = True
    dest18.is_sale = True
    dest18.date_of_sale = '2024-11-11'

    dest19 = Product()
    dest19.title = 'Electric Scooter'
    dest19.price = 700
    dest19.description = 'Eco-friendly electric scooter with long battery life.'
    dest19.category = 'Electronics'
    dest19.image = 'ev.png'
    dest19.sold = False
    dest19.is_sale = False
    dest19.date_of_sale = None

    dest20 = Product()
    dest20.title = 'Fitness Tracker'
    dest20.price = 60
    dest20.description = 'Wearable fitness tracker with sleep monitoring.'
    dest20.category = 'Fitness'
    dest20.image = 'fitnesstracker.png'
    dest20.sold = True
    dest20.is_sale = True
    dest20.date_of_sale = '2024-11-19'
    
    dests =[dest1,dest2,dest3,dest4,dest5,dest6,dest7,dest8,dest9,dest10,dest11,dest12,dest13,dest14,dest15,dest16,dest17,dest18,dest19,dest20]
    
    return render(request, "home.html", {'dests': dests})

def search(request):
    search_query = request.GET.get('q', '')
    
    if search_query:
        products = Product.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    
    context = {
        'products': products,
        'search_query': search_query
    }
    
    return render(request, 'search.html', context)

def filter_products(request):
    # Get filter parameters from the request
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    on_sale = request.GET.get('on_sale')

    # Start with all products
    products = Product.objects.all()

    # Apply filters based on user input
    if category:
        products = products.filter(category=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if on_sale == 'true':  # Checkbox values are typically 'true' or 'false'
        products = products.filter(is_sale=True)

    return products
