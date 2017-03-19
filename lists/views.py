from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()

    context = {'items': items}
    return render(request, 'list.html', context)

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

