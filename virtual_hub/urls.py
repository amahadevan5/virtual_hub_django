from django.urls import path, include

urlpatterns = [
    # include urls from the maps app
    path('maps/', include('maps.urls')),
    
    # include urls from the reports app
    path('reports/', include('reports.urls')),
    
    # default admin url
    path('admin/', admin.site.urls),

    # individual county maps
    path('county/<int:pk>/', views.CountyDetailView.as_view(), name='county-detail'),
    
]
