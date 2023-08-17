from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'TankTuning',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'TankTuning - Каталог',
        'products': [
            {
                'image': '/static/vendor/img/products/spare_wheelshell.png',
                'name': 'Крышка запасного колеса',
                'price': 34999,
                'description': 'Обеспечивает защиту от внешних факторов и кражи.',
                'title': 'Крышка запасного колеса'
            },
            {
                'image': '/static/vendor/img/products/решетка_радиатора.png',
                'name': 'Решетка радиатора tank 300',
                'price': 44999,
                'description': 'Абсолютно новая, глянцевая, с электроникой. Отверстия в решетке небольшие, что является существенным преимуществом в сравнении с оригинальной деталью.',
                'title': 'Решетка радиатора tank 300'
            },
            {
                'image': '/static/vendor/img/products/решетка_радиатора_tank500.png',
                'name': 'Решетка радиатора Tank-500',
                'price': 47999,
                'description': ' ',
                'title': 'Решетка радиатора Tank-500'
            },
            
            {
                'image': '/static/vendor/img/products/амортизаторы_дверей.png',
                'name': 'Амортизаторы дверей',
                'price': 499,
                'description': 'Подходят для багажника и дверей. Обеспечивают бесшумное и плавное закрытие дверей.',
                'title': 'Амортизаторы дверей'
            },
            {
                'image': '/static/vendor/img/products/дверная_ручка.png',
                'name': 'Комплект дверных ручек',
                'price': 3499,
                'description': 'Комплект дверных ручек, для четырех боковых дверей. Выполнены в черном глубоком глянцевом цвете, хромированные. В комплекте идут с креплением.',
                'title': 'Комплект дверных ручек'
            },
            {
                'image': '/static/vendor/img/products/накладка_эмблемы_решетки-радиатора_танк300.png',
                'name': 'Накладка эмблемы решетки радиатора Tank 300',
                'price': 2999,
                'description': 'Придаст вашему Tank 300 брутальный, стильный вид.',
                'title': 'Накладка эмблемы'
            },
            {
                'image': '/static/vendor/img/products/крышка_для_замка.png',
                'name': 'Крышка для замка',
                'price': 3499,
                'description': 'Изготовлены из высококачественной нержавеющей стали и АБС-пластика.',
                'title': 'Крышка для замка'
            },

            {
                'image': '/static/vendor/img/products/обложка_удостоверения.png',
                'name': 'Обложка для водительского удостоверения',
                'price': 899,
                'description': 'Многофункциональное портмоне: для водительского удостоверения, дисконтных и банковских карт.',
                'title': 'Обложка для водительского удостоверения'
            }
        ]
    }
    return render(request, 'products/products.html', context)