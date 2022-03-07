FROM python:buster

WORKDIR /usr/src/app
COPY src/* ./
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]