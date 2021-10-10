import os

from flask_script import Server, Manager
from app import create_app
from mongoengine import connect

#connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1
connect("eyespot", host=os.environ.get("MDB", "mongodb+srv://user:password@host/database?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE&maxPoolsize=1&socketKeepAlive=true"), alias="default")

app = create_app()
manager = Manager(app)


server = Server(host="0.0.0.0", port=5000)

manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
