FROM debian:stable

# Install Python, pip, virtualenv, build tools, SQLite development headers, and Python development headers
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    build-essential libsqlite3-dev wget libpq-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /venv

# Activate the virtual environment (for subsequent commands)
ENV PATH="/venv/bin:${PATH}"

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Get the latest stable SQLite version (you might not need this anymore if solely using PostgreSQL)
RUN wget https://www.sqlite.org/2024/sqlite-autoconf-3450100.tar.gz && \
    tar xzf sqlite-autoconf-3450100.tar.gz && \
    cd sqlite-autoconf-3450100 && \
    ./configure --prefix=/usr/local && \
    make install && \
    rm -rf /app/sqlite-autoconf-3450100*

# Verify the system SQLite version (optional)
RUN /usr/local/bin/sqlite3 --version

# Install Python dependencies within the virtual environment (this will install psycopg2-binary)
RUN pip install --no-cache-dir -r requirements.txt

# Run Django migrations during the build process (psycopg2 should now be available)
RUN python manage.py migrate

# You likely don't need to force reinstall pysqlite3 if you're moving to PostgreSQL
# # Force reinstall of pysqlite3 within the virtual environment, linking against the newer SQLite
# RUN pip uninstall -y pysqlite3 && \
#     LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" pip install --no-cache-dir pysqlite3 --no-binary :all:

# Verify Python sqlite3 version within the virtual environment (optional)
RUN python -c "import sqlite3; print(sqlite3.sqlite_version)"

# Make port 8000 available
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]