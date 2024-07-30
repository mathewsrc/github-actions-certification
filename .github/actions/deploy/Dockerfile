FROM: python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests beautifulsoup4 polars ruff pytest

COPY deployment.py /deployment.py

CMD ["python", "/deployment.py"] 
