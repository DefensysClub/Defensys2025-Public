FROM python:3.10-slim

# Install PHP and necessary extensions
RUN apt-get update && apt-get install -y \
    php \
    php-cli \
    php-fpm \
    php-mysqli \
    php-curl \
    php-xml \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy challenge files into the container
COPY challenge /app

# Expose port 80 (default HTTP port)
EXPOSE 80

# Command to run the PHP built-in server (or use a web server like Apache)
CMD ["php", "-S", "0.0.0.0:80", "-t", "/app"]

