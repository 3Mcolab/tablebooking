from django.shortcuts import render
from Booking.models import EventBook
from .models import Chef, Slider
from Menu.models import MenuItems, MenuCategory

def IndexPage(request):
    events=EventBook.objects.all()
    chefs=Chef.objects.all()
    sliders=Slider.objects.all()
    meal_lists=MenuItems.objects.all()
    categories=MenuCategory.objects.all()
    context={'events':events,'chefs':chefs,'sliders':sliders,
            'meal_lists':meal_lists,'categories':categories}
    return render(request, 'index.html',context)
