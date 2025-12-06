FROM python3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r --no-cache-dir requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3.10", "main.py"]