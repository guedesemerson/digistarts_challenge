from django.urls import path
from .views import ExecuteAlgorithmNumberApi, UpdateRegister, RetrieveRegister, DeleteRegister, ListRegister

urlpatterns = [
    path('execute_algorithm/', ExecuteAlgorithmNumberApi.as_view()),
    path('update_register/<int:id>', UpdateRegister.as_view()),
    path('retrieve-register/<int:id>', RetrieveRegister.as_view()),
    path('delete_register/<int:id>', DeleteRegister.as_view()),
    path('list_register/', ListRegister.as_view()),

]