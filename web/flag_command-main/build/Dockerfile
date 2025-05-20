FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Create a fake flag and a real flag
RUN echo "DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}" > /app/flag

# Make the flag readable only by root
RUN chown root:root /app/flag && chmod 444 /app/flag

# Create a user with UID 1000 
RUN useradd --no-create-home -u 1000 user
USER user
# Expose the port the app runs on
EXPOSE 5000


CMD ["python", "app.py"]