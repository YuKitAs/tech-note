# Simple Webapp in Docker Container

The following tutorial shows how to run a simple webapp created with Python and Redis in a Docker container.

1. Create a project directory.

2. In the project root, we need to create a `Dockerfile`. In this example the configurations are like this:

    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:2.7-slim

    # Set the working directory in the container to `/app`
    WORKDIR /app

    # Copy the current directory to `/app` in the container
    ADD . /app

    # Install any needed packages specified in requirements.txt with Pip
    RUN pip install --trusted-host pypi.python.org -r requirements.txt

    # Make port 80 available to the world outside this container
    EXPOSE 80

    # Define environment variable
    ENV NAME World

    # Run `app.py` when the container launches
    CMD ["python", "app.py"]
    ```

  From above we can see that we need to create a `requirements.txt` for `pip` and a Python file `app.py`.

3. In `requirements.txt`, add two libraries `Flask` and `Redis`.

4. The content of `app.py` looks like this (from official tutorial):

    ```python
    from flask import Flask
    from redis import Redis, RedisError
    import os
    import socket

    # Connect to Redis
    redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

    app = Flask(__name__)

    @app.route("/")
    def hello():
        try:
            visits = redis.incr("counter")
        except RedisError:
            visits = "<i>cannot connect to Redis, counter disabled</i>"

        html = "<h3>Hello {name}!</h3>" \
               "<b>Hostname:</b> {hostname}<br/>" \
               "<b>Visits:</b> {visits}"
        return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)
    ```

5. After having `Dockerfile`, `app.py` and `requirements.txt` in the project root, run `docker build` command to create a Docker image:

    ```console
    $ docker build -t hello-world .
    ```

    Without tagging with `-t`, the image name would be `<none>`, then we can only access the image with its ID (use `docker images` to check image ID).

6. Map machine's port 4000 to the container's published port 80 and run the image we built in the last step:

    ```console
    $ docker run -p 4000:80 hello-world
    ```

7. Go to `http://localhost:4000` in a browser or use `curl http://localhost:4000` to view the app.
