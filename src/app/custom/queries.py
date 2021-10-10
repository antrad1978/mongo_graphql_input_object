from core.pandoro_roles import pandoro_role_secure

from app.generated.types import *
import json

PAGE_SIZE = 15
ALL_STATUS = 0


def skip_page(page):
    return (page - 1) * PAGE_SIZE


def number_pages(records):
    return (records + PAGE_SIZE - 1) / PAGE_SIZE


@pandoro_role_secure("Administrator,SuperAdmin,admin")
def resolve_users_func():
    return list(UserModel.objects.all())


def resolve_user_func(username):
    return UserModel.objects.get(username=username)


def resolve_user_by_id_func(id):
    return UserModel.objects.get(id=id)


def resolve_user_by_username_func(username):
    return UserModel.objects.get(username=username)


def resolve_study_by_id_func(study_id):
    return SampleModel.objects.get(id=study_id)


def resolve_samples_func():
    return list(SampleModel.objects.all())
