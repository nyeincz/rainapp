FROM python:3.10
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "./run.py"]