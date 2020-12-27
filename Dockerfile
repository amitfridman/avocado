# escape=`

FROM python:3
COPY requirements.txt /
COPY "Avocado/" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
RUN chown :www-data Avocado_site/ 
RUN chown :www-data Avocado_site/db.sqlite3
RUN chmod 664 Avocado_site/db.sqlite3
USER 1001
WORKDIR  /Avocado_site/
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
