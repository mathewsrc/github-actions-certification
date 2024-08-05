FROM python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests polars ruff 

COPY ./main.py main.py

CMD ["python", "./main.py"]