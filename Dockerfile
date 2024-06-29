# Use an official Python runtime as a parent image
FROM public.ecr.aws/docker/library/python:3.11.6-slim-bullseye

# Install lambda web adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app ./app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose port 8000
EXPOSE 8000

# Run uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
