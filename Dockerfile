FROM python:slim
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "./run.py"]