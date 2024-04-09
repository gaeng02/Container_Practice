FROM python:3.11
RUN pip install Flask
COPY . /app
CMD ["python", "/app/init_db.py"]
EXPOSE 5001