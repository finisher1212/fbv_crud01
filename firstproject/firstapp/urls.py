from . import views
from django.urls import path

urlpatterns = [
    path('', views.prodlistview, name = 'allprods'),
    path('allprod/', views.addprodview, name = 'addprod'),
    path('delprod/<int:i>/', views.deleteprodview, name = 'del'),
    path('updtprod/<int:oid>/', views.updateprodview, name = 'updt')
]