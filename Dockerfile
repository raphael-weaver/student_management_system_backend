FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /student_management_system_backend

WORKDIR /student_management_system_backend

COPY requirements.txt /student_management_system_backend/

RUN pip install -Ur requirements.txt

COPY . /student_management_system_backend/