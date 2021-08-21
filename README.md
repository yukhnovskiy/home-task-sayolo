# home-task-sayolo
Sayolo home task
Application design is following:
1) we have 2 main get web services adget and impression
2) each service has implemented logic inside for return and for iterating with db
3) sqllite db is started and cleaned up during starting an app
4) from IDE app is starting by running python main.py with uncommenting proper lines, or by creating a docker image and running docker container:
- docker build . --tag sayolo
- docker run -d --name mycontainer -p 80:80 sayolo
5) logic for iterating with db is described in dal package
6) db configuration in db.cofig
7) db models and tables structures are described in db.models.models
8) in db tables there is minimum number of columns with sdk and user premium keys
9) the service logic is following, depending on the get request pass we get a number value from db and increment it or create a new one
10) fastapi framework was chosen as it can hendle asgi async requests
