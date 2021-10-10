from flask_jwt_extended import jwt_required

from app.custom.queries import *
import graphene


class Query(graphene.ObjectType):
    users = graphene.List(User)
    me = graphene.Field(User)
    user = graphene.Field(User, username=graphene.Argument(graphene.ID, required=True), description="Get single user")
    user_by_id = graphene.Field(User, id=graphene.Argument(graphene.ID, required=True), description="Get single user")
    user_by_username = graphene.Field(User, username=graphene.String())
    samples = graphene.List(Sample, username=graphene.String())

    # @jwt_required
    def resolve_users(self, info):
        return resolve_users_func()

    @jwt_required
    def resolve_user(self, info, username):
        return resolve_user_func(username)


    #@jwt_required
    def resolve_user_by_username(self, info, username):
        return resolve_user_by_username_func(username)

    @jwt_required
    def resolve_me(self, info):
        if not hasattr(info.context, 'user'):
            raise Exception('Not logged in!')
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

        # @jwt_required
        def resolve_studies(self, info):
            return resolve_users_func()

    # @jwt_required
    def resolve_samples(self, info):
         return resolve_samples_func()
