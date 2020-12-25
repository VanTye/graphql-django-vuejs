import graphene

from graphene_django import DjangoObjectType
from .models import City, EmployeeTitle, Employee
from graphene_django.filter import DjangoFilterConnectionField


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


class Mutation(graphene.AbstractType):
    create_title = CreateTitle.Field()


