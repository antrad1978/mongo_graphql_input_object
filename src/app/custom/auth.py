import json
import graphene
from core.pandoro_hashing import PandoroHash
from flask_jwt_extended import create_access_token

from mongo.models import User as UserModel
from mongo.models import Group as GroupModel


class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()
    role = graphene.String()
    username = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    @staticmethod
    def mutate(self, info, username, password):
        user = UserModel.objects.get(username=username)
        pass_hash = PandoroHash.hashed(password)

        if not user or user.password != pass_hash:
            raise Exception('Username or password not correct.')
        groups = GroupModel.objects(users=username)
        groups = map(lambda x: x.name, groups)
        data = {"username": username, "role": user.role, "groups": list(groups)}
        return AuthMutation(
            access_token=create_access_token(json.dumps(data)),
            role=user.role,
            username=username
        )
