# big-data-project

## Code
The folder 'scraping' contains the code for scraping tweets (main.py) and cleaning the columns (cleaner.py)  
Please run the files in that order.

## Hadoop
Prerequisites:  
1- Use a Linux-based operating system.  
2- Navigate to the Hive folder (containing the .env and .yml files) before running the commands.  

### 1- Gaining admin permission  
    sudo groupadd docker  
    sudo gpasswd -a $USER docker  
    sudo chmod 666 /var/run/docker.sock  

### 2- Running Docker  
    docker-compose up

### 3- Accessing the uploaded database
    docker stats  
    docker exec -it hive-server /bin/bash  
    hive  
    select * from pfizerdatabase.pfizer  
    
reference: https://hshirodkar.medium.com/apache-hive-on-docker-4d7280ac6f8e

