# Use Python 3.12 on a lightweight Linux base
FROM python:3.12-slim


# Set the working directory inside the container
# WORKDIR defines the current folder for the following Docker commands; /app is just a common folder name and can be changed
WORKDIR /app


# Copy dependency list
# COPY uses: COPY <source> <destination>; here requirements.txt comes from the project folder, and . means the current Docker working directory (/app)
COPY requirements.txt .


# Install Python dependencies
# RUN executes a command while building the image; -r means read package names from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files into the container
# The first . means the current project folder on the computer; the second . means the current Docker working directory (/app)
COPY . .


# Start the FastAPI server
# CMD defines the command that runs when the container starts; app:app means app.py -> app = FastAPI()
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]