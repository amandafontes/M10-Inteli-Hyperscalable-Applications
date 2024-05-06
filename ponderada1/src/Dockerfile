FROM python:3.10.12
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD main.py /app
EXPOSE 5000
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]