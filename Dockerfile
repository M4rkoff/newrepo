FROM python:3

WORKDIR /app

COPY word_counter.py /app/word_counter.py

CMD ["python", "/app/word_counter.py"]
