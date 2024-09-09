# Compile Python dependencies ----------------------------------------------
#
# We use this build stage to compile code while installing Python
# dependencies. Separating this step keeps build tools out of the
# final image, making it cleaner.

FROM docker.io/python:3.11-alpine as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Make use of virtualenv, to cleanly install Python requirements, without
# triggering the ugly "WARNING: Running pip as the 'root' user can result
# in broken permissions and conflicting behaviour".
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install requirements.
COPY requirements /tmp
RUN apk add --no-cache build-base libffi libffi-dev
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

# Create final image -------------------------------------------------------

FROM docker.io/python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy virtual environment from the builder stage
COPY --from=builder /venv /venv

# Set the virtual environment as the default Python environment
ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

# Install app
WORKDIR /app
COPY ./src /app
RUN addgroup app && \
    adduser -D -u 1000 -G app app && \
    chown -R root:app /app
USER app:app
ENV PYTHONPATH /app

# Run app
EXPOSE 5005/tcp
ENTRYPOINT ["python3", "-m", "cli_app"]
