# escape=`

FROM python:3
COPY requirements.txt /
COPY "Avocado/" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
RUN pip install --index-url https://test.pypi.org/simple/ --no-deps avocado_model_amitfr==0.0.6
WORKDIR  /Avocado_site/
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
USER 0
RUN chmod 777 db.sqlite3
# RUN chown root:www-data /Avocado_site
# RUN chown root:www-data /Avocado_site/db.sqlite3
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
