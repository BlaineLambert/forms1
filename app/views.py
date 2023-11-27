from django.shortcuts import render
from app.forms import Hey_form, Age_form, Order_form

# Create your views here.

def page(request):
    if request.GET:
        x = int(request.GET['numberone'])
        y = int(request.GET['numbertwo'])
        answer = x + y
        return render(request, 'index.html', {'x': x, 'y': y, 'answer': answer})
    else:
        return render(request, 'index.html')
    
def hey_you(request):
    form = Hey_form(request.GET)
    if form.is_valid():
        input = form.cleaned_data['word']
        return render(request, 'hey_you.html', {'input': input})
    else:
        return render(request, 'hey_you.html')

def how_old(request):
    form = Age_form(request.GET)
    if form.is_valid():
        current_year = form.cleaned_data['current_year']
        year_born = form.cleaned_data['year_born']
        age = current_year - year_born
        return render(request, 'how_old.html', {'current_year': current_year, 'year_born': year_born, 'age': age})
    else:
        return render(request, 'how_old.html')
    
def order(request):
    form = Order_form(request.GET)
    if form.is_valid():
        burbers = form.cleaned_data['burbers']
        fries = form.cleaned_data['fries']
        drinks = form.cleaned_data['drinks']
        total = (burbers * 4.5) + (fries * 1.5) + (drinks)
        return render(request, 'order.html', {'burbers': burbers, 'fries': fries, 'drinks': drinks, 'total': total})
    else:
        return render(request, 'order.html')