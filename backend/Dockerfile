
FROM python:3.11-slim


LABEL maintainer="devops@example.com"
LABEL description="Backend service for Effective Mobile test task"


RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY app.py .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')" || exit 1

CMD ["python", "app.py"]
