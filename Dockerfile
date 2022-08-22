# docker build . -t app && docker run --rm --interactive app
FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip3 install requests
ADD ./power_sum /power_sum
CMD [ "python3", "./power_sum/main.py" ]