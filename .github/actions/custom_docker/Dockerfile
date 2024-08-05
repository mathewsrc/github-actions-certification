FROM python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests beautifulsoup4 polars ruff pytest

COPY ./main.py main.py

CMD ["python", "main.py"]