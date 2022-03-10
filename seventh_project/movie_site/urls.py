
from django.urls import path
from . import views
app_name = "movie_site"


urlpatterns = [
    path('home/',views.home, name="home"),
    path('detail/<int:id>/', views.detailpage, name="detail"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>', views.edit_review, name="edit_review"),
    path('delreview/<int:movie_id>/<int:review_id>', views.delete_review, name="delete_review"),
]

