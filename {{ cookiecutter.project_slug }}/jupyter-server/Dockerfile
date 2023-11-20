# use quay.io/jupyter/minimal-notebook as base image
FROM quay.io/jupyter/minimal-notebook

# install packages
USER root
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt