# rainapp
Rain Fall App , will generate rainfall data of a particular location in Singapore.

# Install and Run Project

$git clone gitURL
$cd rainapp
$pip install -r requirements.txt
$python run.py

You can see the result by localhost:8080 on your local browser.


# How to run the tests?

$cd pytest
$pytest configtest.py


# How to run Dockerize the application?

Build docker image
Run fullowling command in directory Dockerfile exist.

$docker build -t rainapp:v1 .

