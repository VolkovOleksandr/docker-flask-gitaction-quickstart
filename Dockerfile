FROM python:3.8

WORKDIR '/app'

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python", "application.py", "-env=prod"]
