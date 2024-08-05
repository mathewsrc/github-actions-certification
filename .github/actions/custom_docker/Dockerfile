FROM python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests polars ruff 

# Github action directory (defalt: /github/workspace)
WORKDIR /action 

COPY ./main.py /action/main.py

CMD ["python", "/action/main.py"]