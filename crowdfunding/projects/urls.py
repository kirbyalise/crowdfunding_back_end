from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view())
]
