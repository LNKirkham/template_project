FROM python:3.7-slim-buster

USER $USERNAME
ENV PATH="/home/$USERNAME/.local/bin:${PATH}"

# Set working directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy base image directory to app directory
COPY src /app/template_module/src
COPY tests /app/template_module/tests

# Run script to start app
CMD ["python3", "src/__main__.py"]
