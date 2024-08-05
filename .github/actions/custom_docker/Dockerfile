FROM python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests polars ruff 

COPY main.py /main.py

# post entrypoint
COPY post_entrypoint.sh /post_entrypoint.sh

RUN ls 

CMD ["python", "main.py"]