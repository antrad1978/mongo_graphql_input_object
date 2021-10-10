from mongo.models import User as UserModel
from mongo.models import Sample as SampleModel
from graphene_mongo import MongoengineObjectType


class User(MongoengineObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('password',)


class Sample(MongoengineObjectType):
    class Meta:
        model = SampleModel



