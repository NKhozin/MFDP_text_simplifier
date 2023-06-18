FROM python:3.10.11
WORKDIR .
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main_bot.py"]