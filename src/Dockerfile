# Use an official Python runtime as an image
FROM python:3.7

COPY . /usr/src/app
COPY ./external/pandoro_core-1.0.0-py3-none-any.whl /usr/src/app/external/pandoro_core-1.0.0-py3-none-any.whl
# Copy all essentials file
COPY ./requirements.txt /usr/src/app/requirements.txt

# Work Directory
WORKDIR /usr/src/app

# Install requirements
RUN pip install -r requirements.txt

# Copy the rest
COPY . /usr/src/app

# Expose Port
EXPOSE 5000

# Start application
CMD [ "python", "/usr/src/app/manage.py", "runserver" ]

