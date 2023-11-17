ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

FROM python:3.10

ENV DB_USERNAME=postgres
ENV DB_PASSWORD=mypassword
ENV DB_HOST=sample-database
ENV DB_PORT=5432

RUN echo args ${DB_USERNAME} ${DB_PASSWORD} ${DB_HOST} ${DB_PORT}

# Copy the current directory contents into the container
COPY src/ src/
COPY requirements.txt .
COPY app.py .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000


