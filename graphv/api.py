import uuid
import pydantic
import graphene
import uvicorn
from graphene_pydantic import PydanticObjectType
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class PersonModel(pydantic.BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str


class Person(PydanticObjectType):
    class Meta:
        model = PersonModel
        # exclude specified fields
        exclude_fields = ("id",)


class Query(graphene.ObjectType):
    people = graphene.List(Person)

    @staticmethod
    def resolve_people(parent, info):
        # fetch actual PersonModels here
        return [PersonModel(id=uuid.uuid4(), first_name="Beth", last_name="Smith")]


schema = graphene.Schema(query=Query)


def serve_application():
    app = FastAPI()
    app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))  # , mutation=Mutations)))
    uvicorn.run(app, host="0.0.0.0", port=8000)
