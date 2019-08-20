from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SaleItem

# Create your views here.
def commTrackerView(request):
    total_comp = 0
    all_sale_items = SaleItem.objects.all()
    for item in all_sale_items:
        item_comp = 0
        payoutValue = 0
        number_sold = item.numberSold
        product_sold = item.productSold
        if product_sold == "DirecTV":
            payoutValue = 105.00
        elif product_sold == "Voice GA":
            payoutValue = 30.00
        elif product_sold == "Prepaid":
            payoutValue = 15.00
        total_comp += float(number_sold * payoutValue)
    return render(request, 'index.html', {'all_items': all_sale_items,'total_commission': total_comp})

def addSale(request):
    new_item = SaleItem(numberSold = request.POST['numberSold'], productSold = request.POST['productSold'],)
    new_item.save()
    return HttpResponseRedirect('/commissiontracker/')