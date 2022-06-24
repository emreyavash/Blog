from .models import Category

def category(request):
    categories = Category.objects.filter(status = True)
    return {'categories':categories}