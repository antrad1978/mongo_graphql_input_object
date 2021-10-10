from flask_cors import CORS
from flask_graphql_auth import GraphQLAuth
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_graphql import GraphQLView

from app.generated.mutations import Mutation
from app.generated.queries import Query
from app.generated.types import *
import graphene


app = Flask(__name__)


def create_app():
    app.config.from_object("config." + app.config["ENV"].capitalize() + "Config")

    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = '76753288aecbc1234568dcba'  # Change this!
    JWTManager(app)

    schema = graphene.Schema(query=Query, mutation=Mutation, types=[User])

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        pass

    GraphQLAuth(app)

    return app

