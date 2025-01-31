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
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
from matplotlib.dates import DateFormatter
import urllib 
from matplotlib.ticker import MaxNLocator


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})



# View to render the table
def product_table(request):
    # Define all 20 product entries
    products = Product.objects.all()
    return render(request, "product_table.html", {"products": products})

def search(request):
    query = request.GET.get('q')  # Get search query from URL parameters
    products = Product.objects.all()  # Fetch all products
    if query:
        products = Product.objects.filter(title__icontains=query)  # Apply search filter
     # Debugging: Print filtered products

    return render(request, 'search.html', {'products': products})



def filter_products(request):
    # Get filter parameters from request
    category = request.GET.get('category')
    sold = request.GET.get('sold')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Get all products initially
    products = Product.objects.all()

    # Apply filters if selected
    if category:
        products = products.filter(category=category)

    if sold:
        products = products.filter(sold=(sold.lower() == 'true'))

    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, "products.html", {"products": products, "categories": categories})



# View to render the graph
def sales_chart(request):
    # Fetch only products that have been sold and have a sale date
    products = Product.objects.filter(sold=True, date_of_sale__isnull=False).values("category", "price", "date_of_sale")

    if not products.exists():
        return render(request, "category_chart.html", {"error": "No sold products found."})

    # Convert to DataFrame
    df = pd.DataFrame(list(products))

    # Debug: Print the data to check if 'price' is valid
    print(df)

    # Ensure the price column is numeric, and handle any non-numeric values (NaN)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Drop rows with NaN prices (if any)
    df = df.dropna(subset=["price"])

    # Convert date_of_sale to datetime
    df["date_of_sale"] = pd.to_datetime(df["date_of_sale"])

    # Extract 'Year-Month' for grouping
    df["month_year"] = df["date_of_sale"].dt.strftime("%Y-%m")

    # Group by Category and Month-Year, summing the sales amount (Price)
    sales_data = df.groupby(["category", "month_year"])["price"].sum().unstack(fill_value=0)

    # Check if sales_data is empty
    if sales_data.empty:
        return render(request, "category_chart.html", {"error": "No valid sales data found."})

    # Create the column chart
    plt.figure(figsize=(10, 6))
    sales_data.plot(kind="bar", stacked=False, colormap="viridis")
    plt.title("Category-Wise Sales Amount (Monthly)")
    plt.xlabel("Month")
    plt.ylabel("Total Sales Amount (₹)")
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Set y-axis to integer values
    plt.legend(title="Category")
    plt.tight_layout()

    # Save plot to a memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    # Convert plot to image URL (base64 encoded)
    graph_url = f"data:image/png;base64,{string}"

    return render(request, "category_chart.html", {"graph_url": graph_url})


def total_items_chart(request):
    # Fetch only products that have been sold with a sale date
    products = Product.objects.filter(sold=True, date_of_sale__isnull=False).values("category", "date_of_sale")

    if not products.exists():
        return render(request, "total_items_chart.html", {"error": " "})

    # Convert to DataFrame
    df = pd.DataFrame(list(products))

    # Debug: Print DataFrame to console
    print(df)

    # Convert date_of_sale to datetime
    df["date_of_sale"] = pd.to_datetime(df["date_of_sale"], errors="coerce")

    # Drop invalid dates
    df = df.dropna(subset=["date_of_sale"])

    # Extract 'Year-Month' for grouping
    df["month"] = df["date_of_sale"].dt.strftime("%Y-%m")

    # Count total items per category per month
    item_count_data = df.groupby(["month", "category"]).size().unstack()

    # Debug: Print grouped data
    print(item_count_data)

    # If there's no data, show error message
    if item_count_data.empty:
        return render(request, "total_items_chart.html", {"error": "No sold items found."})

    # Create the column chart (which is a vertical bar chart)
    plt.figure(figsize=(10, 6))
    item_count_data.plot(kind="bar", stacked=True, colormap="viridis")
    plt.xlabel("Month")
    plt.ylabel("Total Items Sold")
    plt.title("Total Items in Each Category (Monthly)")
    plt.xticks(rotation=45)
    plt.legend(title="Category")
    plt.tight_layout()

    # Save plot to a memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    # Convert plot to image URL
    graph_url = f"data:image/png;base64,{string}"

    return render(request, "total_items_chart.html", {"graph_url": graph_url})


