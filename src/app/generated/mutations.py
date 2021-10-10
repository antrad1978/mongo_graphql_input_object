from flask_graphql_auth import mutation_jwt_required, query_header_jwt_required, mutation_header_jwt_required
from flask_jwt_extended import jwt_required

from app.custom.types import *
from app.custom.auth import AuthMutation
from app.custom.mutations import *


class DeleteUser(graphene.Mutation):
    user = graphene.Boolean()

    class Arguments:
        user_data = graphene.String()

    @jwt_required
    def mutate(self, info, user_data):
        user = delete_user(user_data)
        return DeleteUser(user=user)


class CreateSample(graphene.Mutation):
    sample = graphene.Field(Sample)

    class Arguments:
        sample_data = SampleInput()

    #@jwt_required
    def mutate(self, info, sample_data):
        sample = save_study_func(sample_data)
        return CreateSample(sample=sample)


class UpdateSample(graphene.Mutation):
    sample = graphene.Field(Sample)

    class Arguments:
        sample_data = SampleInput()

    #@jwt_required
    def mutate(self, info, sample_data):
        sample = update_study(sample_data)
        return SampleInput(sample=sample)


class DeleteSample(graphene.Mutation):
    res = graphene.Boolean()

    class Arguments:
        sample_id = graphene.String(required=True)

    #@jwt_required
    def mutate(self, info, sample_id):
        res = delete_sample(sample_id)
        return DeleteSample(res=res)


class Mutation(graphene.ObjectType):
    create_user = UserInput.mutate
    delete_user = DeleteUser.Field()
    create_sample = CreateSample.Field()
    update_sample = UpdateSample.Field()
    delete_sample = DeleteSample.Field()




