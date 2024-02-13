from django.shortcuts import render

# Create your views here.
def cart_summery(request):
    return render(request, 'cart_summery.html', {})


def cart_add(request):
    pass

def cart_remove(request):
    pass

def cart_update(request):
    pass
