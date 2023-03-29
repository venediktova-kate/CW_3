FROM python:3.10

ENV HOME /app
WORKDIR $HOME

COPY requrements.txt .
RUN python3 -m pip install --no-cache -r requrements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]