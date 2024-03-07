FROM python:3.10.13-bookworm

RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
RUN apt-get update && apt-get install gcc pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic -y

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code

CMD ["bash"]
