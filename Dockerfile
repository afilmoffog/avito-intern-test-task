FROM python:3.6-alpine

RUN adduser -D appuser

WORKDIR /home/appuser

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./app

RUN chown -R appuser:appuser ./
USER appuser

EXPOSE 5000
ENTRYPOINT ["python"]

CMD ["app/app.py"]