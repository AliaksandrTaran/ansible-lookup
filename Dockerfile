FROM sbeliakou/centos:7.3
FROM python:2.7
RUN pip install ansible
RUN mkdir -p /ansible/playbooks
WORKDIR /ansible/playbooks/
CMD ["ansible-playbook","lookup.yml"]
