Set MDB env var to set proper string connection to MongoDB.

connect("myapp", host=os.environ.get("MDB", "mongodb+srv://login:password@host/db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"), alias="default")

To run project configure Pycharm with Flask support or run manage.py file.
Connect to url /graphql to see graphiql UI.


#How to build Docker image 
To build image, from main folder run (Dockerfile_local_requirements):

docker build -t app/backend:v1 .

To run a container instance:

docker run -p 80:80/tcp app/backend:v1

To run a shell on container:

docker exec -it backend bash

