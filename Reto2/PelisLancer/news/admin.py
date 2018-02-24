from django.contrib import admin

from .models import peliculas,usuario
# Register your models here.

@admin.register(peliculas)
class  pelisAdmin(admin.ModelAdmin):
	list_display = ('titulo','imagen','genero', 'precio', 'director', 'pais',)

#admin.site.register(peliculas, pelisAdmin)
	

@admin.register(usuario)
class  usuarioAdmin(admin.ModelAdmin):
	pass
#admin.site.register(usuario, usuarioAdmin)
