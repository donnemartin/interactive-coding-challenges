FROM jupyter/minimal-notebook

USER root

RUN mkdir /notebook && \
    chown $NB_USER /notebook

USER $NB_USER

COPY requirements.txt /notebook

RUN pip install --upgrade pip && \
    pip install -r /notebook/requirements.txt && \
    rm /notebook/requirements.txt
