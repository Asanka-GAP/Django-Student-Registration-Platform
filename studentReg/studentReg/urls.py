from django.contrib import admin
from django.urls import include, path
from members import views as hv

urlpatterns = [
    
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    path('',hv.index,name=''),
    path('show/',hv.show,name='show'),
    path('index/',hv.index,name='index'),
    path('register/',hv.register,name='register'),
    path('addrecord/',hv.addRecord,name='addrecord'),
    path('delete/<int:id>',hv.delete,name='delete'),
    path('update/<int:id>',hv.update,name='update'),
    path('updaterecord/<int:id>',hv.updaterecord,name='updaterecord'),
]