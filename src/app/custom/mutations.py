# This file contains all mutations implementation code
import os
import ssl
import uuid
from datetime import datetime, timedelta

from core.pandoro_hashing import PandoroHash
from flask_jwt_extended import jwt_required

from app.custom.types import *
from app.generated.types import *
from mongo.mapper import MongoMapper
from mongo.utility import HashHelper

context = ssl._create_unverified_context()


@jwt_required
def create_user_func(args):
    new_user = UserModel(**args)
    new_user.password = HashHelper.hashed(new_user.password)
    new_user.save()
    return new_user


def delete_user(user_data):
    user = UserModel.objects.get(id=user_data)
    user.delete()
    return True


def save_study_func(args):
    sample = SampleModel()
    MongoMapper.map_dict(sample, args)
    #study.user = logged_user()
    sample.save()
    return sample


def update_study(sample_data):
    study = SampleModel.objects.get(id=sample_data.id)
    MongoMapper.map_dict(study, sample_data)
    study.save()
    return study


def delete_sample(sample_id):
    sample = SampleModel.objects.get(id=sample_id)
    sample.delete()
    return True
