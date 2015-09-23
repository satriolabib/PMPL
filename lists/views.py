from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	#items = Item.objects.all()
	return render(request, 'home.html')

def view_list(request, list_id):
	#list_ = List.objects.get(id=list_id)
	items = Item.objects.all()#filter(list=list_)
	return render(request, 'list.html', {'items': items})

