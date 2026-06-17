from django.urls import path
from .views import home
from .views import Find_A_Peer
from .views import home
from .views import AI_page
from .views import g
from .views import home
from .views import sign_up_as_a_peer
from .views import criteria
from .views import funds
from .views import donations
from .views import partners
from .views import foreign_currencies
urlpatterns = [
    path("AI/",AI_page),
    path("FindAPeer/",Find_A_Peer),
    path("",home),
    path("Sign_up_as_a_peer", sign_up_as_a_peer),
    path("criteria", criteria),
    path("funds", funds),
    path("donations", donations),
    path("partners",partners),
    path("foreign_currencies/",  foreign_currencies),

]
