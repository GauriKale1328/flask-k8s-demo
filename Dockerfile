# 1. Base image: small official Python image
FROM python:3.12-slim

# 2. Version label shown in the app (override with --build-arg)
ARG APP_VERSION=v1
ENV APP_VERSION=$APP_VERSION

# 3. Working directory inside the container
WORKDIR /app

# 4. Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Document the port the app listens on
EXPOSE 5000

# 7. Start the app
CMD ["python", "app.py"]
