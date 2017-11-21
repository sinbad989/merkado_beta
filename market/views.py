from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # paginator lib

# Create your views here.
def home(request):
	return render(request,'market/home.html',{})

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.all()

	paginator = Paginator(products, 3) # paginate the queryset into 3 pages.
	page = request.GET.get('page')

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	# paginator division creator
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request,'market/product/list.html',{'category':category,'categories':categories,'products':products,'page':page})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug)
	return render(request,"market/product/detail.html",{'product':product,})

def about(request):
	return render(request,'market/about.html',{})
