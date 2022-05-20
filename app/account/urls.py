from django.urls import path
from .views import add_customskill, signup, log_in, log_out, home, add_skill

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('addskill/', add_skill, name='add_skill'),
    path('addcustomskill/', add_customskill, name='add_customskill')
]