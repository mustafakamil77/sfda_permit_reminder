# urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('',views.AllPermit,name='index'),
     path('about',views.About,name='about'),
     path('connect',views.Connect,name='Connect'),
     path('form',views.PermitForm,name='new_form'),
     path('EditSdfaPermit/<int:SdfaPermit_id>/',views.Edit_Permit,name='EditSdfaPermit'),
     path('Delete_Sdfa_Permit/<int:Delete_SdfaPermit>/',views.DeleteSdfaPermit,name='delete_permit'),


]