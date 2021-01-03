import graphene

from graphene_django import DjangoObjectType
from .models import City, EmployeeTitle, Employee
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id # for updating


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        filter_fields = ['city_name']
        interfaces = (graphene.relay.Node,)


class EmployeeTitleNode(DjangoObjectType):
    class Meta:
        model = EmployeeTitle
        filter_fields = ['title_name']
        interfaces = (graphene.relay.Node,)

class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = [
            'employee_name',
            'employee_city__city_name',
            'employee_title__title_name'
        ]
        interfaces = (graphene.relay.Node,)

class Query(object):
    city = graphene.relay.Node.Field(CityNode)
    all_cities = DjangoFilterConnectionField(CityNode)

    employee_title = graphene.relay.Node.Field(EmployeeTitleNode)
    all_titles = DjangoFilterConnectionField(EmployeeTitleNode)

    employee = graphene.relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)


class CreateTitle(graphene.relay.ClientIDMutation):
    title = graphene.Field(EmployeeTitleNode)

    class Input:
        title_name = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        title = EmployeeTitle(title_name=input.get('title_name'))
        title.save()

        return CreateTitle(title=title)


class CreateEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        employee_name = graphene.String()
        employee_city = graphene.String()
        employee_title = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employee = Employee(
            employee_name=input.get('employee_name'), 
            employee_city=City.objects.get(city_name=input.get('employee_city')),
            employee_title=EmployeeTitle.objects.get(title_name=input.get('employee_title'))
        )
        employee.save()
        return CreateEmployee(employee=employee)


class UpdateEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        id = graphene.String()
        employee_name = graphene.String()
        employee_city = graphene.String()
        employee_title = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employee = Employee.objects.get(pk=from_global_id(input.get('id'))[1])
        employee.employee_name = input.get('employee_name')
        employee.employee_city = City.objects.get(city_name=input.get('employee_city'))
        employee.employee_title = EmployeeTitle.objects.get(title_name=input.get('employee_title'))
        employee.save() 
        return UpdateEmployee(employee=employee)


class DeleteEmployee(graphene.relay.ClientIDMutation):
    employee = graphene.Field(EmployeeNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        employee = Employee.objects.get(pk=from_global_id(input.get('id'))[1])
        employee.delete()
        return DeleteEmployee(employee=employee)


class Mutation(graphene.AbstractType):
    create_title = CreateTitle.Field()
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()



