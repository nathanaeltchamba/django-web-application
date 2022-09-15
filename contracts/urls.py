from django.urls import path 
from .views import (ContractCreateView, ContractRetrieveView, ContractUpdateView, ContractDeleteView)

app_name = "contracts"

urlpatterns = [
    path('contract/<pk>/', ContractRetrieveView.as_view(), name="contract-detail"),
    path('contract/<pk>/update', ContractUpdateView.as_view(), name="contract-update"),
    path('contract/<pk>/delete', ContractDeleteView.as_view(), name="contract-delete"),
    path('add-contract', ContractCreateView.as_view(), name="contract-create"),
]