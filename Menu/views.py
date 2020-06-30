from django.shortcuts import render
from .models import MenuItems, MenuCategory

def MenuPage(request):
    menu_lists=MenuItems.objects.all()
    categories=MenuCategory.objects.all()
    context={'menu_lists':menu_lists,'categories':categories}

    return render(request,'menu-list.html',context)
