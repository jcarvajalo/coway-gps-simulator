FROM python:3
WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install  -r /src/requirements.txt

COPY . /src/

CMD ["python", "simulator.py"]