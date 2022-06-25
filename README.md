# compose-dev-env


How to setup and build
1. docker-compose up # keep it up for the services
2. Get a shell into the container:
    ```shell
    docker-compose exec app # Or any other service name
    ```
3. Run the app
    ```shell
    python3 main.py
    ```

MongoDB will be ready for the app...   
You can access the app on port 8000 from the browser - http://localhost:8000  
In addition MongoExpress will run on port 8081 so you can navigate the db through the browser - http://localhost:8081  

All the credentials listed in the .env file