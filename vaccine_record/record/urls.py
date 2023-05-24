from django.urls import path
from . import views
from record.views import ContactWizard,multiStepForm,register,form_list,user_logout,user_login,form_list,Form_saved,self_view,createForm,update_form,relative_update_form,delete,relative_delete_form,medical_news
from django.urls import include
from record.forms import UserProfileInfo, vaccine



urlpatterns = [
path('', views.index, name='index'),
path('formsubmission/', views.multiStepForm.as_view(), name= 'form_submission' ),
path('', ContactWizard.as_view([UserProfileInfo, vaccine])),
path('registration/', views.register, name= 'register'),
path('create/', views.createForm, name= 'create'),
path('update/<uuid:vaccine_info_id>/', views.update_form, name='update_form'),
path('relative_update/<uuid:relative_vaccine_info_id>/',views.relative_update_form, name='relative_update_form'),
path ('login/', views.user_login, name= 'login'),
path('Saved/', views.form_list, name= 'form_list'),
path('logout/',views.user_logout, name= 'logout'),
path('form_saved/',views.form_list, name='form_list'),
path('warnings/', views.delete, name= 'warnings'),
  path('medical-news/', views.medical_news, name='medical_news'),
path('relative_delete/<uuid:relative_vaccine_info_id>/', views.relative_delete_form, name='relative_delete_form'),
path('delete/<uuid:vaccine_info_id>/', views.delete_form, name='delete'),
path('display/',views.Form_saved, name='form_saved'),
path('self/',views.self_view, name='self_form'),
]
