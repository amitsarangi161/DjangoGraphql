import graphene
from .models import Todo
from graphene_django import DjangoObjectType


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ("id", "name", "status", "created_at")


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType, id=graphene.Int(), page_no=graphene.Int())

    def resolve_todos(root, ino, id=None, page_no=None):
        if not id:
            print(page_no)
            return Todo.objects.all()
        else:
            return Todo.objects.filter(id=id)


class DeleteTodo(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return DeleteTodo(message=f"Deleted Id is {id} ")


class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        name = graphene.String(required=True)
        status = graphene.Boolean(required=True)

    def mutate(self, info, name, status):
        todo = Todo(name=name, status=status)
        todo.save()
        return CreateTodo(todo=todo)


class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        status = graphene.Boolean(required=True)
    def mutate(self, info, id, name, status):
        todo = Todo.objects.get(id=id)
        todo.name = name
        todo.status = status
        todo.save()
        return UpdateTodo(todo=todo)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
