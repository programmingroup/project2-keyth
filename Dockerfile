FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /project2-keyth

COPY . /project2-keyth

EXPOSE 5000

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "passwordgen.py"]