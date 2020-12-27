# escape=`

FROM python:3
COPY requirements.txt /
COPY "djangoProject1" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
WORKDIR  /Avocado_site/Avocado/
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]