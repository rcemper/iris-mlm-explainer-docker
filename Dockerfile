ARG IMAGE=jupyter/base-notebook
FROM $IMAGE
USER root
COPY ./requirements.txt /tmp/requirements.txt
#  RUN pip install -U "jupyter-server<2.0.0"
RUN pip3 install -r /tmp/requirements.txt
