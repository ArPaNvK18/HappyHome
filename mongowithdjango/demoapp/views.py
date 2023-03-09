from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from demoapp.models import Todo,MoneyExpence

# Create your views here.
def home(request):
    # retrive money from database
    retrive_price = MoneyExpence.objects.values('prise')
    # print(retrive_price.get('prise'))
    count = 0
    for i in retrive_price:
        # print(i)
        count = count+i.get('prise')
        # print(count)
    return render(request,'home.html',{'count':count})

def submit(request):
    # Retrive data from frontend
    Title = request.POST.get('title')
    DESC = request.POST.get('desc')
    Date = request.POST.get('date')
    Price = request.POST.get('price')
    data = {'title':Title,'desc':DESC, 'date':Date, 'price':Price}
    # print(data)
    moneyExpence = MoneyExpence(reason=Title , description = DESC, date = Date, prise = Price)
    # save it in database
    moneyExpence.save()
    return render(request,'submit.html')

def histry(request):
    chk_histry = MoneyExpence.objects.values()
    return render(request,'history.html',{'list':chk_histry})