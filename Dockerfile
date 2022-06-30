FROM centos
FROM python:3.8
RUN git clone https://github.com/sunxiangyu0528/dev07.git
WORKDIR /dev07
RUN pip install -i  https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip  && pip3 install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 9000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:9000"]
