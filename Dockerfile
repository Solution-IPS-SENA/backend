FROM python:3.9
ARG SRC_PATH
WORKDIR /app
COPY ${SRC_PATH} .
RUN pip install -r requirements.txt
CMD [ "python3", "wsgi.py" ]