FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt
COPY . /app

EXPOSE 5000

RUN chmod +x run_main.sh
CMD [ "python", "flaskapi.py" ]
#CMD ["/app/run_main.sh"]
