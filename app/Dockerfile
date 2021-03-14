FROM python:3.6.8-alpine3.9

ENV GROUP_ID=1000 \
    USER_ID=1000

# Sets the working directory
WORKDIR /var/www/

RUN python -m pip install --upgrade pip

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /var/www/
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the source code into the container
COPY . /var/www/
 
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]