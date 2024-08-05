FROM python:3.12-slim

RUN python -m pip install --upgrade pip

RUN pip install requests polars ruff 

COPY main.py /main.py

COPY post_entrypoint.sh /post_entrypoint.sh
RUN chmod +x /post_entrypoint.sh

# /post_entrypoint.sh must to be added to PATH
ENV PATH="/:${PATH}"

CMD ["python", "/main.py"]