# our base image
FROM alpine:latest

# Install python and pip
RUN apk add --update py-pip

RUN python -m venv /usr/src/app/venv
RUN source /usr/src/app/venv/bin/activate

# upgrade pip
RUN /usr/src/app/venv/bin/pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r /usr/src/app/requirements.txt
# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["/usr/src/app/venv/bin/python", "/usr/src/app/app.py"]
