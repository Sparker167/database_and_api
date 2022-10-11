FROM python:latest

WORKDIR /app

COPY requirements.txt /app/.

COPY app.py /app/.
COPY create_populate_table.py /app/.
COPY Pokemon.csv /app/.


RUN pip install -r requirements.txt


EXPOSE 5000


CMD [ "python", "app.py" ]


