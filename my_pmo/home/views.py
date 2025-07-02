from django.shortcuts import render

# Create your views here.
def vista_home(request):
    # Lógica para la página de inicio, si es necesaria
    context = {
        'welcome_message': 'Bienvenido a nuestro sitio!',
        # Otros datos dinámicos
    }
    return render(request, 'home.html', context)