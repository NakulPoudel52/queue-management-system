from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('Home', views.home),
    path('Signup', views.signup),
    path('Contact', views.contact),
    path('Hospital', views.hospital),
    path('Bank', views.bank),
    path('Feed', views.feed,name="feed"),
	path('download/', views.index1,name="download"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('dfrm/', views.dfrm_view,name="dfrm"),
]
