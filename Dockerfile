# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
FROM python:3.13-slim

WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install the package
RUN pip install --upgrade pip \
    && pip install .

EXPOSE 8000

CMD ["python", "server.py"]
