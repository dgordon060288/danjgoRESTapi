FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py migrate
#RUN python manage.py createsuperuser --email dan.gordon@darkwolfsolutions.com --username admin
RUN echo password
RUN echo y
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]