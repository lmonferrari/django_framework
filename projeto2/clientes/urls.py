from django.urls import path

from .views import person_create, person_delete, person_edit, person_list

urlpatterns = [
    path('list/', person_list, name="list"),
    path('create/', person_create, name="create"),
    path('edit/<int:id>', person_edit, name='edit'),
    path('delete/<int:id>', person_delete, name='delete')
]
