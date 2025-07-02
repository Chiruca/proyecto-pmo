from django.db import models

# Create your models here.

class MarcoMetodo(models.Model):
    Marco_tipo = models.CharField(max_length=100)
    Marco_nom = models.CharField(max_length=200)
    Marco_desc = models.TextField(blank=True)
    def __str__(self):
        return '%s %s %s'%(self.Marco_tipo, self.Marco_nom, self.Marco_desc)

class MarcoObs(models.Model):
    Marc_Obs_orden = models.IntegerField(default=0)
    Marc_Obs_nom = models.CharField(max_length=200)
    Marc_Obs_desc = models.TextField(blank=True)
    Marco_ID = models.ForeignKey(MarcoMetodo, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s'%(self.Marc_Obs_orden, self.Marc_Obs_nom, self.Marc_Obs_desc)
    
class PPV(models.Model):
    PPV_tipo = models.CharField(max_length=100)
    PPV_nom = models.CharField(max_length=100)
    PPV_obj = models.TextField()
    PPV_desc = models.TextField(blank=True)
    Marco_ID = models.ForeignKey(MarcoMetodo, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s'%(self.PPV_tipo, self.PPV_nom, self.PPV_obj, self.PPV_desc)   

class Rol(models.Model):
  Rol_nom = models.CharField(max_length=100)
  Rol_desc = models.TextField(blank=True)
  Marco_ID = models.ForeignKey(MarcoMetodo, null=True, on_delete=models.CASCADE)
  def __str__(self):
    return '%s %s'%(self.Rol_nom, self.Rol_desc)
  
class DomEco(models.Model):
    DomEco_nom = models.CharField(max_length=100)
    DomEco_desc = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return '%s %s'%(self.DomEco_nom, self.DomEco_desc)
    
class EcoTarea(models.Model):
    EcoTarea_orden = models.IntegerField(default=0)
    EcoTarea_nom = models.CharField(max_length=100)
    EcoTarea_desc= models.CharField(max_length=100)
    EcoTarea_obs = models.TextField(blank=True)
    TRoles = models.ManyToManyField(Rol)
    DomEco_ID = models.ForeignKey(DomEco, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s'%(self.EcoTarea_orden, self.EcoTarea_nom, self.EcoTarea_desc, self.EcoTarea_obs)
    
class EcoFacilitador(models.Model):
    EcoFacilitador_orden = models.IntegerField(default=0)
    EcoFacilitador_nom = models.CharField(max_length=100)
    EcoFacilitador_obs = models.TextField()
    FRoles = models.ManyToManyField(Rol)
    EcoTarea_ID = models.ForeignKey(EcoTarea, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s'%(self.EcoFacilitador_orden, self.EcoFacilitador_nom, self.EcoFacilitador_obs)
    
class DomDes(models.Model):
    DomDes_nom = models.CharField(max_length=100)
    DomDes_obj = models.CharField(max_length=100)
    DomDes_ben = models.TextField()
    DomEco_ID = models.ForeignKey(DomEco, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s'%(self.DomDes_nom, self.DomDes_obj, self.DomDes_ben)
    
class DomDesComent(models.Model):
    DomDesComent_orden = models.IntegerField(default=0)
    DomDesComent_tit = models.CharField(max_length=100)
    DomDesComent_desc = models.TextField(blank=True)
    DomDes_Url = models.URLField(max_length=200, blank=True, null=True)
    DomDes_ID = models.ForeignKey(DomDes, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s'%(self.DomDesComent_orden, self.DomDesComent_tit, self.DomDesComent_desc, self.DomDes_Url)
    
class MMA(models.Model):
    MMA_tipo = models.CharField(max_length=50)
    MMA_clase = models.CharField(max_length=200)
    MMA_nom = models.CharField(max_length=200)
    MMA_desc = models.TextField(blank=True)
    DominiosDes = models.ManyToManyField(DomDes)
    Marcos = models.ManyToManyField(MarcoMetodo)
    def __str__(self):
        return '%s %s %s %s'%(self.MMA_tipo, self.MMA_clase,self.MMA_nom, self.MMA_desc)
    
class MMAElement(models.Model):
    MMAElem_orden = models.IntegerField(default=0)
    MMAElem_nom = models.CharField(max_length=200)
    MMAElem_desc = models.TextField(blank=True)
    MMAElem_Url = models.URLField(max_length=200, blank=True, null=True)
    MMA_ID = models.ForeignKey(MMA, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s'%(self.MMAElem_orden, self.MMAElem_nom, self.MMAElem_desc, self.MMAElem_Url)