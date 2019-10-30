# Hello World Birthday

## Overview
Simple application to show birthday message.

## Requirements
Python 3.6
docker
docker-compose

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
docker-compose up
```

## Amazon ECS deployment with AWS CodePipeline

Deployment strategy is Rolling Update. 

```
http://helloworldbirthday-lb-2098004525.us-east-2.elb.amazonaws.com/ui
```

![Alt text](pipeline.png?raw=true "AWS CodePipeline")

Traffic to container balanced via AWS LoadBalancer.

![Alt text](AWSTG.png?raw=true "AWS TG")
![Alt text](AWSTargets.png?raw=true "AWSTargets")
