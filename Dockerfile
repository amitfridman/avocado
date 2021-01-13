# escape=`

FROM python:3
COPY requirements.txt /
COPY "Avocado/" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
RUN pip install --index-url https://test.pypi.org/simple/ --no-deps avocado_model_amitfr==0.0.6
WORKDIR  /Avocado_site/
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN chown :www-data  /
RUN chown :www-data db.sqlite3
RUN chmod 664 db.sqlite3
USER 1001
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
