FROM centos:centos8
USER 0
RUN sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/*.repo &&\
    sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/*.repo &&\
    sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/*.repo
#RUN yum update && yum upgrade -y
RUN yum install -y python3 openssh-server sudo && /usr/bin/ssh-keygen -A

#RUN /bin/bash /etc/init.d/sshd start
#RUN /bin/bash mkdir /var/run/sshd
#RUN /bin/bash mkdir /usr/sbin/sshd
#RUN /bin/bash mkdir /usr/ssh/
#RUN /bin/bash touch /usr/ssh/sshd_config
#RUN /bin/bash echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
#RUN /bin/bash echo 'root:toor' | chpasswd
#RUN /bin/bash -c yum install -y initscripts
#RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
#RUN /bin/bash sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
#RUN /bin/bash sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config
#RUN /bin/bash sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config


EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

