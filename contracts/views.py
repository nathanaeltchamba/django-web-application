from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Contract, User
from .forms import ContractForm, CustomUserCreationForm

# Create your views here.

# CRUD + L - create, retrieve, update, delete, list

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class ContractListView(generic.ListView):
    template_name = "contracts.html"
    queryset = Contract.objects.all()

    context_object_name = "contracts"

    # def get_queryset(self):
    #     pass 

class ContractRetrieveView(LoginRequiredMixin, generic.DetailView):
    template_name = "contract.html"
    queryset = Contract.objects.all()

    context_object_name = "contract"

class ContractCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "contract_create.html"
    form_class = ContractForm

    def get_success_url(self):
        return reverse('contract-list')

class ContractUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "contract_update.html"
    queryset = Contract.objects.all()
    form_class = ContractForm

    def get_success_url(self):
        return reverse('contract-list')


class ContractDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "contract_delete.html"
    queryset = Contract.objects.all()

    def get_success_url(self):
        return reverse('contract-list')

