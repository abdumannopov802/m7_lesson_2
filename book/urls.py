from django.urls import path
from .views import *

urlpatterns = [
    path('', Book_list_view.as_view(), name='book-list'),
    path('book-detail/<int:pk>/', Book_detail_view.as_view(), name='book-detail'),
    path('book-create/', Book_create_veiw.as_view(), name='book-create'),
    path('book-update/<int:pk>', Book_update_view.as_view(), name='book-update'),
    path('book-delete/<int:pk>', Book_delete_view.as_view(), name='book-delete'),
]
