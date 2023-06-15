from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'))),
    path('producto/', include(("producto.urls", "producto"))),
    path('cliente/', include(("cliente.urls", "cliente"))),
    path('aboutus/', include(("aboutus.urls", "aboutus"))),
    #path('contacto/', include(("contacto.urls", "contacto"))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)