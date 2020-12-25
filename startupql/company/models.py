from django.db import models


# City where employees live
class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class EmployeeTitle(models.Model):
    title_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_city = models.ForeignKey(City, related_name='employee', null=True, on_delete=models.SET_NULL)
    employee_title = models.ForeignKey(EmployeeTitle, related_name='employee', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.employee_name
