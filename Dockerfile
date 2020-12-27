# escape=`

FROM python:3
COPY requirements.txt /
COPY "Avocado/" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
RUN chgrp -R 0 /db.sqlite3 \
  && chmod -R g+rwx /db.sqlite3
USER 1001
WORKDIR  /Avocado_site/
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
