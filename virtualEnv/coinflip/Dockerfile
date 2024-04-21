FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping 
RUN pip install Pillow
RUN pip install daphne



COPY . .

EXPOSE 8080

CMD ["daphne", "coinflip.asgi:application", "--bind", "0.0.0.0", "--port", "8080"]