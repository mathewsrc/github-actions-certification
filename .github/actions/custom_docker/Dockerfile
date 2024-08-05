FROM python:3.12-slim

#WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install requests polars ruff 

#COPY main.py /app/main.py
COPY main.py /main.py

# post entrypoint
#COPY post_entrypoint.sh /app/post_entrypoint.sh
#RUN chmod +x /app/post_entrypoint.sh

COPY post_entrypoint.sh /post_entrypoint.sh
RUN chmod +x /post_entrypoint.sh

# Add /app to PATH
#ENV PATH="/app:${PATH}"

#CMD ["python", "/app/main.py"]

CMD ["python", "/main.py"]