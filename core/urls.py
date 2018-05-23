from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_client', views.register_client, name='register'),

	#path('', views.IndexView.as_view(), name='index'),
	# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# path('<int:pk>/results/', views.ResultsView.as_view(), name='result'),
	# path('<int:question_id>/vote/', views.vote, name='vote'),
]
