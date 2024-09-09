ARG PYTHON_IMAGE=docker.io/python:3.12-alpine

# ============================================================================
# Target: builder
# ============================================================================

FROM ${PYTHON_IMAGE} AS builder

# Don't let Python cache files end up in the venv.
ENV PYTHONPYCACHEPREFIX=/tmp/.python_cache

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
RUN python3 -m pip install --no-compile --no-cache-dir -r /tmp/requirements.txt


# ============================================================================
# Target: app-base
# ============================================================================

FROM ${PYTHON_IMAGE} AS app-base

# Setup app-group and app-user. Stages derived from this one can use this user
# for running as non-root, without having to depend on a user as provided by
# the base image.
RUN addgroup app-group && adduser -h /app -s /bin/sh -G app-group -S -D app-user

# Copy virtual environment from the builder stage
COPY --from=builder /venv /venv

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Allow for detecting the Docker environment (used to determine the integration
# test configuration to apply.)
RUN touch /.dockerenv


# ============================================================================
# Target: netprov
# ============================================================================

FROM app-base AS netprov

# Install app
WORKDIR /app
COPY ./src /app
USER app-user:app-group
ENV PYTHONPATH /app

# Run app
EXPOSE 5005/tcp
ENTRYPOINT ["python3", "-m", "cli_app"]
