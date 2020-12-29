# escape=`

FROM python:3
COPY requirements.txt /
COPY "Avocado/" "Avocado_site/"
EXPOSE 8000
RUN pip install -r requirements.txt
WORKDIR  /Avocado_site/
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install nodejs
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
RUN npm install -g @angular/cli
RUN python manage.py migrate
RUN chown :www-data  /
RUN chown :www-data db.sqlite3
RUN chmod 664 db.sqlite3
USER 1001
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
