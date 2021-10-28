from django.conf.urls import url
from DjangoAPP.settings import MEDIA_URL
from Livros import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^livros_id$', views.livrosApi),
    url(r'^livros_id/([0-9]+)$',views.livrosApi),

    url(r'^livros$', views.livrosApid),
    url(r'^livros/([0-9]+)$',views.livrosApid),

    url(r'^livros/salvararquivo',views.SalvarArquivo)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)