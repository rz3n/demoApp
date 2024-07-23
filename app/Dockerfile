# /Dockerfile

FROM python:alpine

RUN mkdir /app

WORKDIR /app
EXPOSE 8000

COPY . /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
