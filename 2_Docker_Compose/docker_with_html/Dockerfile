FROM python:3.11
RUN pip install Flask
RUN pip install requests
COPY . /app
CMD ["python", "/app/main.py"]
EXPOSE 5000