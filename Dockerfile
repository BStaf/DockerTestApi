FROM python:3.7-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#RUN ls
CMD ["python", "src/api.py"]
