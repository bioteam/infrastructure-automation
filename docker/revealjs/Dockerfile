# This Dockerfile is expanded from the example given in the talk
# slides. It starts with a Node.js container base.
FROM node

# Next, we install a series of dependencies that are used to power the
# tools used within the demo - Ansible, AWS CLI, Docker client, Docker
# Compose, highlight and aws-cloudformation-stack-status.
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

# This installs the Wetty framework used to embed the live demos into
# the slides.
RUN yarn global add wetty.js

# Next, install the Reveal.js framework and the grunt-connect-proxy
# which is used to proxy the Wetty server behind the main Reveal.js
# endpoint.
RUN git clone https://github.com/hakimel/reveal.js.git && \
    cd reveal.js && npm install && \
    mkdir slides && \
    npm install grunt-connect-proxy

RUN apt-get -y install screen

# Now, add in a number of files from this repository.
ADD gruntfile.js /reveal.js/gruntfile.js
ADD index.html /reveal.js/index.html
ADD slides/slides.md /reveal.js/slides/slides.md
ADD bashrc /root/.bashrc
ADD run.sh /run.sh

# Finally, configure the container by exposing its port and defining
# the run script and its working directory.
EXPOSE 8000
WORKDIR /reveal.js
CMD ["/bin/bash", "/run.sh"]

