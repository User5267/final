FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip freeze > requirements.txt

WORKDIR C:/Users/Ахмедияр/Desktop/pythonpr
# install app
COPY . app

# final configuration
ENV FLASK_APP=app
EXPOSE 5432
CMD ["python3", "app.py"]