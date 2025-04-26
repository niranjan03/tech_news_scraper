FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]  # For web server
# OR for scraper:
# CMD ["python", "app/run_scraper.py"]