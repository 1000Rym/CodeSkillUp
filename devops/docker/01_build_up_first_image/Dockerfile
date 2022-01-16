FROM python:alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apk add --no-cache bash
EXPOSE 3000
ENTRYPOINT [ "python", "./launch.py"] 
