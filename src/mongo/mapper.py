from flask_graphql_auth import get_jwt_identity
import json


class MongoMapper:
    @staticmethod
    def map_dict(source, data: dict):
        for key in data:
            if key != 'id':
                setattr(source, key, data[key])
        return source


def logged_user() -> str:
    user = json.loads(get_jwt_identity())
    return user['username']
