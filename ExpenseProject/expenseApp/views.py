from django.shortcuts import render
from rest_framework import generics
from expenseApp.serializers import ExpenseSerializer
from expenseApp.models import Expense

# Create your views here.
class ExpenseListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
    serializer_class = ExpenseSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)