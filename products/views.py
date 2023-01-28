from django.shortcuts import render
from products.models import ProductCategory, Poduct


# Create your views here.
# controllers (functions)


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store-Каталог',
        'products': Poduct.objects.all(),
        'categories': ProductCategory.objects.all(),
        # [
        #     {'image': '/static/vendor/img/products/Adidas-hoodie.png',
        #      'name': 'Худи черного цвета с монограммами adidas Originals',
        #      'price': 6090,
        #      'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      },
        #     {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
        #      'name': 'Синяя куртка The North Face',
        #      'price': 2372,
        #      'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
        #      },
        #     {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        #      'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #      'price': 3390,
        #      'description': 'Плотная ткань. Легкий материал.',
        #      },
        # ]
    }
    return render(request, 'products/products.html', context)
