from django.urls import path
from companies.views.employees import Employees, EmployeeDetail

urlpatterns = [
    path('employees', Employees.as_view()),
    path('employess/<int:employee_id>', EmployeeDetail.as_view())
]
