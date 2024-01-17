from django.urls import path
from oweapp.views import airline_views

urlpatterns = [
  
    path('travellar/create/',airline_views.create,name='createtravellar'),
    path('travellar/store/',airline_views.store,name='storetravellar'),
    path('travellar/index/',airline_views.index,name='indextravellar'),
    path('travellar/updateview/<int:pk>',airline_views.updateview,name='edittravellarview'),
    path('travellar/update/<int:pk>',airline_views.update,name='edittravellar'),

    
    path('Airlines/create/',airline_views.createairlines,name='createairlines'),
    path('Airlines/store/',airline_views.storeairlines,name='storeairlines'),
    path('Airlines/index/',airline_views.indexairlines,name='indexairlines'),
    path('Airlines/updateview/<int:pk>',airline_views.updateviewairlines,name='editairlinesview'),
    path('Airlines/update/<int:pk>',airline_views.updateairlines,name='editairlines'),
 

  
    path('Crew/create/',airline_views.createcrew,name='createcrew'),
    path('Crew/store/',airline_views.storecrew,name='storecrew'),
    path('Crew/index/',airline_views.indexcrew,name='indexcrew'),
    path('Crew/updateview/<int:pk>',airline_views.updateviewcrew,name='editcrewview'),
    path('Crew/update/<int:pk>',airline_views.updatecrew,name='editcrew'),

    path('Riskaction/create/',airline_views.createriskaction,name='createriskaction'),
    path('Riskaction/store/',airline_views.storeriskaction,name='storeriskaction'),
    path('Riskaction/index/',airline_views.indexriskaction,name='indexriskaction'),
    path('Riskaction/updateview/<int:pk>',airline_views.updateviewriskaction,name='editriskactionview'),
    path('Riskaction/update/<int:pk>',airline_views.updateriskaction,name='editriskaction'),

    path('Journeysearch/create/',airline_views.createjourneysearch,name='createjourneysearch'),
    path('Journeysearch/store/',airline_views.storejourneysearch,name='storejourneysearch'),
    path('Journeysearch/index/',airline_views.indexjourneysearch,name='indexjourneysearch'),
    path('Journeysearch/updateview/<int:pk>',airline_views.updateviewjourneysearch,name='editjourneysearchview'),
    path('Journeysearch/update/<int:pk>',airline_views.updatejourneysearch,name='editjourneysearch'),
]
