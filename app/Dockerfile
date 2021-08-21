FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

#COPY . C:/sayolo
WORKDIR  ./app/app


COPY ./app/requirements.txt ./app/requirements.txt

#RUN pip3 install -r requirements.txt

RUN pip install -r ./app/requirements.txt

COPY . .

# Set environment varibles
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

#EXPOSE 80

#CMD [ "python", "app/main.py", "--host=127.0.0.1"]
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

