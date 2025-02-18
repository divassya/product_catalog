from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Handle search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Handle category filter
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category_id=category_filter)

    # Handle tag filter
    tag_filter = request.GET.get('tags')
    if tag_filter:
        products = products.filter(tags__id=tag_filter)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
        'category_filter': category_filter,
        'tag_filter': tag_filter,
        'search_query': search_query
    })
