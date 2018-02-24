from django.db import models
from django.utils.html import format_html

# Create your models here.


class peliculas(models.Model):
	titulo = models.CharField(max_length=70)
	genero = models.CharField(max_length=70)
	imagen = models.ImageField(upload_to='pelis-image',null=True)
	Cliente = models.ForeignKey("usuario", on_delete=models.CASCADE, null = True)
	fecha_Alquier = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
	fechaDevolucion = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
	precio = models.DecimalField(max_digits=6, decimal_places=2,null=True)
	Sinópsis = models.TextField(null=True)
	director = models.CharField(max_length=70,null = False)
	pais = models.CharField(max_length=70,null = False)
 
def image_tag (self):
    	return format_html(" <image src='{}' />".format(self.image.url))
    	image_tag.allow_tags = True






class usuario(models.Model):
   nombre = models.CharField(max_length=70) 
   apellido = models.CharField(max_length=70)
   foto = models.ImageField(upload_to='usuario-image',null = True)
   create_at = models.DateTimeField(auto_now=False, auto_now_add=False,null = True)
   update_at = models.DateTimeField(auto_now=False, auto_now_add=False,null = True)
   TarjetaCredito = models.CharField(max_length=19, null = True)
 
   def __str__ (self):
    return "%s %s" % (self.nombre, self.apellido)

      
class Alquiler (models.Model):
	cliente = models.ForeignKey(usuario, null = True, blank = True,on_delete=models.CASCADE)
	cantidad_pelicula =models.IntegerField(null=True)
	f_debuelta = models.DateTimeField(null = True)
    