# Specify our container base image
FROM python:3.10

# Select a directory within our container
WORKDIR /usr/app

# Copy everything from our project root into our WORK DIRECTORY directory
COPY . .

# Install dependencies
#RUN pip install -r requirements.txt

# Give our container internet access
#EXPOSE 80

# Execute this command on start
ENTRYPOINT ["python", "-m", "current_project.py"]