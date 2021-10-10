import graphene
from graphene_mongodb import MongoSchema

from app.custom.mutations import create_user_func
from mongo.models import User as UserModel
from mongo.models import Sample as SampleModel
from mongo.mongo_input_object import PandoroMongoInputObjectType


class UserInput(MongoSchema):
    model = UserModel

    @staticmethod
    def mutate(args, context):
        return create_user_func(args)


class AuthInput(graphene.InputObjectType):
    access_token = graphene.String()
    refresh_token = graphene.String()
    role = graphene.String()
    username = graphene.String()


class SampleInput(PandoroMongoInputObjectType):
    class Meta:
        model = SampleModel
