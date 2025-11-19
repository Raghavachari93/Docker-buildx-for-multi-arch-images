FROM python:3.12-slim

# Create and set working directory
WORKDIR /app

# Copy application code
COPY app/ /app/

# Install dependencies (none right now, but this keeps it flexible)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8000

# Default command
CMD ["python", "main.py"]
