from django.contrib import admin
from .models import Rol, DomEco, EcoTarea, EcoFacilitador, MarcoMetodo, MarcoObs, PPV, DomDes, DomDesComent, MMA, MMAElement

# Register your models here.
class MarcoMetodoAdmin(admin.ModelAdmin):
  list_display = ("Marco_tipo", "Marco_nom", "Marco_desc")

class MarcoObsAdmin(admin.ModelAdmin):
  list_display = ("Marc_Obs_orden", "Marc_Obs_nom", "Marc_Obs_desc", "Marco_ID")

class PPVAdmin(admin.ModelAdmin):
  list_display = ("PPV_tipo", "PPV_nom", "PPV_obj", "PPV_desc", "Marco_ID")

class RolAdmin(admin.ModelAdmin):
  list_display = ("Rol_nom", "Rol_desc", "Marco_ID")

class DomEcoAdmin(admin.ModelAdmin):
    list_display = ("DomEco_nom", "DomEco_desc")

class EcoTareaAdmin(admin.ModelAdmin):
    list_display = ("EcoTarea_orden","EcoTarea_nom", "EcoTarea_desc","EcoTarea_obs", "DomEco_ID")

class EcoFacilitadorAdmin(admin.ModelAdmin):
    list_display = ("EcoFacilitador_orden", "EcoFacilitador_nom", "EcoFacilitador_obs", "EcoTarea_ID")

class DomDesAdmin(admin.ModelAdmin):
    list_display = ("DomDes_nom", "DomDes_obj", "DomDes_ben", "DomEco_ID")

class DomDesComentAdmin(admin.ModelAdmin):
    list_display = ("DomDesComent_orden", "DomDesComent_tit", "DomDesComent_desc", "DomDes_Url", "DomDes_ID")

class MMAAdmin(admin.ModelAdmin):
    list_display = ("MMA_tipo", "MMA_clase", "MMA_nom", "MMA_desc")

class MMAElementAdmin(admin.ModelAdmin):
    list_display = ("MMAElem_orden", "MMAElem_nom", "MMAElem_desc", "MMAElem_Url", "MMA_ID")

# Registrar el modelo Rol con su administrador personalizado
admin.site.register(MarcoMetodo, MarcoMetodoAdmin)
admin.site.register(MarcoObs, MarcoObsAdmin)
admin.site.register(PPV, PPVAdmin)

admin.site.register(Rol, RolAdmin)
admin.site.register(DomEco, DomEcoAdmin)
admin.site.register(EcoTarea, EcoTareaAdmin)
admin.site.register(EcoFacilitador, EcoFacilitadorAdmin)

admin.site.register(DomDes, DomDesAdmin)
admin.site.register(DomDesComent, DomDesComentAdmin)
admin.site.register(MMA, MMAAdmin)
admin.site.register(MMAElement, MMAElementAdmin)