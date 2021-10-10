from datetime import datetime, timedelta

import bson
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField, ObjectIdField
from mongoengine.fields import (
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    BooleanField,
    StringField,
    IntField,
    FloatField,
    ObjectIdField
)

class User(Document):
    meta = {"collection": "users", 'indexes': ['email']}
    username = StringField(unique=True, required=True, max_length=256)
    name = StringField()
    email = StringField(unique=True, required=False, sparse=True)
    reset_password_token = StringField()
    reset_password_timeout = DateTimeField()
    company = StringField()
    address = StringField()
    password = StringField(required=True)
    role = StringField(required=True)
    is_active = BooleanField(required=True, default=True)
    is_verified = BooleanField(required=True, default=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField(required=True, default=datetime.now())


class Group(Document):
    meta = {"collection": "groups"}
    name = StringField(unique=True, required=True, max_length=256)
    is_active = BooleanField(required=True, default=True)
    is_verified = BooleanField(required=True, default=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField(required=True, default=datetime.now())
    users = ListField(StringField)


class Sample(Document):
    meta = {"collection": "samples", 'indexes': ['name']}
    name = StringField(required=True)
    user = StringField(required=False)
    language = StringField(required=True)
    text = StringField(required=True)

