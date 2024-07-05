#!/bin/bash

# Pull the Docker image
docker pull Chaitanyabeemanaboina.pythonanywhere.com/chaitanyabeemanaboina_ecommerce:latest

# Stop and remove any existing containers
docker stop chaitanyabeemanaboina_ecommerce || true
docker rm chaitanyabeemanaboina_ecommerce || true

# Run the Docker container
docker run -d --name chaitanyabeemanaboina_ecommerce -p 8000:8000 Chaitanyabeemanaboina.pythonanywhere.com/chaitanyabeemanaboina_ecommerce:latest



#!/bin/bash

# Pull the Docker image
docker pull docker.io/chaitanyabeemanaboina/chaitanyabeemanaboina_ecommerce:latest

# Stop and remove any existing containers
docker stop chaitanyabeemanaboina_ecommerce || true
docker rm chaitanyabeemanaboina_ecommerce || true

# Run the Docker container
docker run -d --name chaitanyabeemanaboina_ecommerce -p 8000:8000 docker.io/chaitanyabeemanaboina/chaitanyabeemanaboina_ecommerce:latest
