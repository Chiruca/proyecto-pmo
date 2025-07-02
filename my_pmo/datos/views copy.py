from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Rol, MarcoMetodo, MarcoObs, DomDes, DomDesComent, MMA, MMAElement

# Create your views here.
def tablas_view(request, tipo):
    marco = MarcoMetodo.objects.get(Marco_nom=tipo)
    if tipo == 'SCRUM':
        Marco_img = '/static/img/scrum.png'
    marco_desc = marco.Marco_desc
    marco_desc = marco_desc.replace('\n', '<br>')  # Reemplazar saltos de línea por <br>
    context = {
        'welcome_message': 'Bienvenidos a la Guía de '+ tipo,
        'marco_desc_message': marco_desc,
        'marco_img': Marco_img if 'Marco_img' in locals() else '',  # Asegura que la variable exista
        'opciones_message': 'EXPLORA NUESTRAS SECCIONES DE ' + tipo + ':',
        'tipo_message': tipo,
    }
    return render (request, 'reportes.html', context)

def roles_view(request, tipo):
    # Selecciona los roles según el tipo de marco
    # Aquí se asume que 'tipo' es el nombre del marco, como 'SCRUM', 'PMBOK', etc.
    # Obtiene el marco de trabajo correspondiente
    pmoroles_tipo = MarcoMetodo.objects.get(Marco_nom=tipo)
    pmoroles= Rol.objects.filter(Marco_ID=pmoroles_tipo).order_by('Rol_nom')
    context = {
        'pmoroles': pmoroles,
        'welcome_message': 'Roles de ' + tipo,
    }
    return render (request, 'all_roles.html', context)

def rol_detail(request, id):
    pmorol = Rol.objects.get(id=id)
    pmorol.Rol_desc = pmorol.Rol_desc.replace('\n', '<br>')
    tipo = pmorol.Marco_ID.Marco_nom if pmorol.Marco_ID else 'Desconocido'
    context = {
        'pmorol': pmorol,
        'tipo': tipo,
    }
    return render(request, 'rol_detail.html', context)

def marco_detail(request, tipo):
    pmomarco = MarcoMetodo.objects.get(Marco_nom=tipo)
    marco_obs = MarcoObs.objects.filter(Marco_ID=pmomarco.id).order_by('Marc_Obs_orden')
    for obs in marco_obs:
        obs.Marc_Obs_desc = obs.Marc_Obs_desc.replace('\n', '<br>')
    template = loader.get_template('metodologia.html')
    context = {
        'pmomarco': pmomarco,
        'marco_obs': marco_obs,
        'tipo_message': tipo,
    }
    return HttpResponse(template.render(context, request))

def domdes_view(request):
    # Muestra los dominios de desempeño indiferentemente del tipo de marco metodológico
    domdes_header = DomDes.objects.get(DomDes_nom='DESCRIPCIÓN GENERAL')
    # Puedes manejar el caso en que domdes_header no exista usando try/except si lo deseas.
    domdes_header.DomDes_ben = domdes_header.DomDes_ben.replace('\n', '<br>')  # Reemplazar saltos de línea por <br>
    # Excluye el dominio de desempeño 'DESCRIPCIÓN GENERAL' y ordena por nombre
    pmodomdes = DomDes.objects.exclude(DomDes_nom='DESCRIPCIÓN GENERAL').order_by('DomDes_nom')
    context = {
        'welcome_message': 'Áreas de Foco en la Gestión de Proyectos',
        'domdes_header': domdes_header,
        'pmodomdes': pmodomdes,
    }
    return render (request, 'all_domdes.html', context)

def domdes_detail(request, id):
    pmodomdes = DomDes.objects.get(id=id)
    pmodomdes.DomDes_desc = pmodomdes.DomDes_desc.replace('\n', '<br>')
    context = {
        'pmodomdes': pmodomdes,
        'id': id,  # Añade el ID al contexto para usar en la plantilla
    }
    return render(request, 'domdes_detail.html', context)

def domdescoment_view(request, id):
    # Muestra el detalle de los comentarios de los dominios de desempeño
    domdescoment = DomDesComent.objects.filter(DomDes_ID=id)
    context = {
        'welcome_message': 'Detalle del Dominio de Desempeño:',
        'domdescoment': domdescoment,
        'id': id,  # Añade el ID al contexto para usar en la plantilla
    }
    return render(request, 'all_domdes_coment.html', context)

# Esta vista es para mostrar el detalle de un comentario específico de un dominio de desempeño.
# Si necesitas mostrar un comentario específico, puedes descomentar y ajustar esta función.
# ---------------------------------------------------------------
# def domdescoment_detail(request, id):
#    domdescoment = DomDesComent.objects.get(id=id)
#    domdescoment.DomDesComent_desc = domdescoment.DomDesComent_desc.replace('\n', '<br>')
#    template = loader.get_template('domdescoment_detail.html')
#    context = {
#        'domdescoment': domdescoment,
#        'id': domdescoment.id,  # Añade el ID al contexto para usar en la plantilla
#    }
#    return HttpResponse(template.render(context, request))
# ---------------------------------------------------------------

def metodos_view(request, tipo):
    # Muestra los Métodos / Eventos de tipo = SCRUM
    try:
        marco = MarcoMetodo.objects.get(Marco_nom=tipo)
    except MarcoMetodo.DoesNotExist:
        return HttpResponse("Marco de trabajo no encontrado.", status=404)
    # Filtra los métodos por tipo y marco
    mmametodos = MMA.objects.filter(MMA_tipo="MÉTODO", Marcos=marco.id).order_by('MMA_nom')

    # Asegúrate de que 'mmametodos' es un queryset o una lista de objetos
    if not mmametodos:
        return HttpResponse("No se encontraron métodos para el tipo especificado.", status=404)
    context = {
        'welcome_message': 'Eventos de: ' + tipo,
        'mmametodos': mmametodos,
    }
    return render (request, 'all_metodos.html', context)

def metodo_detail(request, id):
    pmomma = MMA.objects.get(id=id)
    if not pmomma:
        return HttpResponse("Método no encontrado.", status=404)
    pmomma.MMA_desc = pmomma.MMA_desc.replace('\n', '<br>')  # Reemplazar saltos de línea por <br>

    pmomma_elem = MMAElement.objects.filter(MMA_ID=id)
    if not pmomma_elem:
        return HttpResponse("No se encontraron elementos para el método especificado.", status=404)
    
    # Reemplaza los saltos de línea por <br> en las descripciones de marco_obs
    for elem in pmomma_elem:
        elem.MMAElem_desc = elem.MMAElem_desc.replace('\n', '<br>')  # Reemplazar saltos de línea por <br>
    
    template = loader.get_template('metodo_detail.html')

    # Cargar la imagen del marco de trabajo si es SCRUM

    context = {
        'metodo_message': 'Detalle del Evento:' + pmomma.MMA_nom,
        'pmomma': pmomma,
        'pmomma_elem': pmomma_elem,
        'tipo': 'SCRUM',  # Añade el ID al contexto para usar en la plantilla
    }
    return HttpResponse(template.render(context, request))