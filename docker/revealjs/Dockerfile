FROM node

RUN apt-get update && \
    apt-get -y install python-pip apt-transport-https ca-certificates \
               curl gnupg2 software-properties-common highlight && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get -y install docker-ce-cli bsdmainutils && \
    pip install ansible docker-compose awscli && \
    curl -o /usr/share/highlight/langDefs/yml.lang "https://gitlab.com/saalen/highlight/raw/master/langDefs/yaml.lang?inline=false" && \
    cd /usr/local/share && \
    git clone https://github.com/alestic/aws-cloudformation-stack-status && \
    ln -s /usr/local/share/aws-cloudformation-stack-status/aws-cloudformation-stack-status /usr/local/bin && \
    mkdir /demo

RUN yarn global add wetty.js

RUN git clone https://github.com/hakimel/reveal.js.git && \
    cd reveal.js && npm install && \
    mkdir slides && \
    npm install grunt-connect-proxy

ADD gruntfile.js /reveal.js/gruntfile.js
ADD index.html /reveal.js/index.html
ADD slides/slides.md /reveal.js/slides/slides.md
ADD bashrc /root/.bashrc
ADD run.sh /run.sh

EXPOSE 8000
WORKDIR /reveal.js
CMD ["/bin/bash", "/run.sh"]

