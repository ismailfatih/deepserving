FROM python:3.7-slim-stretch
#FROM pytorch/pytorch:1.3-cuda10.1-cudnn7-runtime

#ENV PATH="/root/miniconda3/bin:${PATH}"
#ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update && \
    apt-get install -y git python3-dev gcc && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# RUN apt-get update && \
# 	apt-get install -y libsndfile1 espeak && \
# 	apt-get clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY app app/

RUN python app/server.py

EXPOSE 5000

CMD ["python", "app/server.py", "serve"]
