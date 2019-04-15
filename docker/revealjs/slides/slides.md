<!-- .slide: data-background-color="#286ee0" -->
## Infrastructure Automation: Real Examples

<br><br><br>

![bioteam](slides/bioteam-wt.png)<!-- 
.element: style="float:left; margin: 0px 50px 0px 150px" -->
Karl Gutwin<br>
*Sr Scientific Consultant, BioTeam*
<!-- .element: style="text-align:left" -->

Note: The goal of this talk is to give practical examples about how
automation for your infrastructure can be both straightforward and
useful in day-to-day scenarios.

---

<!-- .slide: data-background-image="slides/bioteam.png" -->

![robot](slides/Automation_of_foundry_with_robot.jpg)<!-- 
.element: style="float:right" -->
### We live in an automated world

*infrastructure automation is robotics for IT*

Note: Why automation? Robots are better than humans at tedious or
precise tasks that can be clearly defined. Think of infrastructure
automation as robotics for IT - in a few lines of code, you can define
repeatable instructions so that your systems can manage themselves.

---

<!-- .slide: data-background-image="slides/bioteam.png" -->

## Infrastructure as Code

Know the intent and implementation of your system

Note: The most important point - if you can read code and understand
what it does - IaC provides the cleanest way to know the intent and
implementation of your system. Example: Recently I was able to review
some automation I had written for a particular service, and didn't
have to re-learn the "gotchas" I learned the first time around.

---

<!-- .slide: data-background-image="slides/bioteam.png" -->

![lifecycle](slides/Lifecycle.png)<!-- 
.element: style="float:right; height:350px; margin-right:50px" -->
### Automation is more than provisioning

* Managing changes
* Cleanup and deletion

Note: We've all been in the place where we aren't sure how to tear
something down cleanly, or how to track the results of a change.

---

<!-- .slide: data-background-image="slides/bioteam.png" -->

## Why not automation?

* Additional point of failure
* Too clever for its own good
* Code as a liability
* Sometimes additional costs

**These are all risks we currently manage within IT**

Note: Manage these risks like we manage risks from other applications
or systems

---

<!-- .slide: data-background-image="slides/bioteam.png" -->

### Many tools to choose from

_including_
* Ansible
* Docker
* Lambda
* CloudFormation

Note: I'm not particularly endorsing these tools over their rivals. Do
your own testing and evaluation. AWS will be the reference cloud
during this talk, but these concepts apply to Azure and GCP.

---

<!-- .slide: data-background="#286ee0" -->
# Examples

&#x2b91; [github.com/bioteam/infrastructure-automation](https://github.com/bioteam/infrastructure-automation)

Note: Please try these examples yourself. They don't require special
privileges, licenses, or approval to try on your own laptop or in your
own free AWS account.

---

<!-- .slide: data-background="#1f4e9b" -->
## ![ansible](slides/ansible.png) Ansible

Configure your server

Note: Ansible comes from a long line of “configuration management” or
“configuration automation” tools, where the primary goal is to run
something on a server that does things like edit config files, install
packages and enable services. Why do you want this? Because these
tasks are tedious and error-prone to follow for humans, and because
shell scripts tend to be brittle.

---

<!-- .slide: data-background-image="slides/ansible.png" -->

`webserver.yml`

```
---
- hosts: localhost
  tasks:
    - name: install nginx
      package: name=nginx state=present

    - name: set to run on boot
      service: name=nginx enabled=yes state=started
```

Note: Series of steps that declare what you want to have happen.
Ansible figures out the "how". This makes code like this able to run
on a wide range of systems.

---

<!-- .slide: data-background-image="slides/ansible.png" -->

`database.yml`

```
---
- hosts: localhost
  tasks:
    - name: install postgresql
      package: name=postgresql state=present

    - name: update config file
      lineinfile:
        path: /etc/postgresql/9.6/main/postgresql.conf
        regexp: '^synchronous_commit ='
        line: 'synchronous_commit = {{ pg_sync|default("on") }}'
      register: postgres_config

    - name: set to run on boot
      service: name=postgresql enabled=yes state=started

    - name: restart service
      service: name=postgresql state=restarted
      when: postgres_config.changed
```
<!-- .element: class="medium" -->

Note: We can add variables and conditions

---

<!-- .slide: data-background-image="slides/ansible.png" -->

`ansible-playbook database.yml`

<iframe data-src="/wetty" width="100%" height="400px" id="term"></iframe>

---

<!-- .slide: data-background-image="slides/ansible.png" class="get-started" -->

### Get Started

* `pip install ansible`<br>
* [github.com/ansible/ansible-examples](https://github.com/ansible/ansible-examples)<br>
* [docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)

Note: You don't need to install Ansible on your servers - it can
remotely configure any server that it can SSH to.

---

<!-- .slide: data-background="#1f4e9b" -->
## ![docker](slides/docker.png) Docker

Applications in Containers

Note: Docker was introduced to the world as a means of
“containerizing” applications so that all of their dependencies,
libraries and code were contained in an isolated environment. The
concept has been around for a while, but only became practical in the
Linux ecosystem with the tooling that Docker provides. Now Docker, by
itself, is just the engine to run the containers. Today, we'll focus
on the two most simple Docker automation tools: docker builds and
docker compose.

---

<!-- .slide: data-background-image="slides/docker.png" -->

`Dockerfile`

```
FROM node

RUN git clone https://github.com/hakimel/reveal.js.git && \
    cd reveal.js && npm install
    
EXPOSE 8000
WORKDIR /reveal.js
CMD ["npm", "start"]
```

<br>

`docker build -t my-image .`

Note: Given an initial image, run a bunch of commands and set
configuration fields.

---

<!-- .slide: data-background-image="slides/docker.png" -->

`docker-compose.yml`

```
---
version: '3'
services:
  mediawiki:
    image: mediawiki
    restart: always
    ports: ['8080:80']
    links: ['database']
    volumes:
      - /var/www/html/images
#     - ./LocalSettings.php:/var/www/html/LocalSettings.php
  database:
    image: mariadb
    restart: always
    environment:
      MYSQL_DATABASE: my_wiki
      MYSQL_USER: wikiuser
      MYSQL_PASSWORD: example
      MYSQL_RANDOM_ROOT_PASSWORD: 'yes'
```
<!-- .element: class="medium" -->

Note: Docker Compose is the next level of automation in the Docker
world. You can imagine how you might build a “stack” of containers
that all interrelate - in this example, a database connected to a web
server. Docker Compose lets you take those containers (defined as
Dockerfiles) and spin them all up together, and take them down
together. By default, it defines a virtual network that the containers
use to communicate with one another, and it has many more useful
features.

---

<!-- .slide: data-background-image="slides/docker.png" -->

`docker-compose up`

<iframe data-src="/wetty" width="100%" height="400px"></iframe>

---

<!-- .slide: data-background-image="slides/docker.png" class="get-started" -->

### Get Started

* [www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
* [docker-curriculum.com](https://docker-curriculum.com)
* [docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/)

---

<!-- .slide: data-background="#1f4e9b" -->
## ![lambda](slides/lambda.png) Lambda

Event-driven automation

Note: The previous tools were all about the automation of application
management. But Lambda is all about event-driven compute - so why is
it in this talk? Because we can use Lambda to do things automatically
in response to cloud infrastructure events. What do I mean? Let's see
an example.

---

<!-- .slide: data-background-image="slides/lambda.png" -->

`autotag.py`
```
import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    principal_type = event['detail']['userIdentity']['type']
    if principal_type == 'IAMUser':
        username = event['detail']['userIdentity']['userName']
    else:
        username = event['detail']['userIdentity']['principalId']

    response = event['detail']['responseElements']
    instance_ids = [i['instanceId']
                    for i in response['instancesSet']['items']]

    ec2.create_tags(Resources=instance_ids, 
                    Tags=[{"Key": "Owner", "Value": username}])
```
<!-- .element: class="python medium" -->

Note: this is a Lambda function that automatically tags EC2 instances
with the username of the user who launched the instance. I bet there’s
a few folks here who have “mystery” EC2 instances - well, something
like this certainly could help. Here we handle an event coming from
CloudTrail; it has details about the user who invoked the event, and
the resulting EC2 instance IDs, so all we need to do is apply the
appropriate tag.

---

<!-- .slide: data-background-image="slides/lambda.png" -->

`demo-autotag.sh`

<iframe data-src="/wetty" width="100%" height="400px"></iframe>

Note: This type of event-driven management automation goes beyond
metadata augmentation. Imagine that you never want to look up an EC2
IP address again - well, write a Lambda function to manage DNS entries
in Route 53 on instance creation and teardown. Or integrate with your
legacy CMDB so that each instance is tracked by its creator, IP
address, AMI, project, account, etc.

---

<!-- .slide: data-background-image="slides/lambda.png" -->

### Other ideas

* Manage DNS entries
* Integrate with a CMDB
* Automate application rollout
* Automatic health checks for critical applications
* Data pipelines and ETL

---

<!-- .slide: data-background-image="slides/lambda.png" class="get-started" -->

### Get Started

* [docs.aws.amazon.com/AmazonCloudWatch/latest/<wbr>events/CloudWatch-Events-Tutorials.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatch-Events-Tutorials.html)

---

<!-- .slide: data-background="#1f4e9b" -->
## ![cfn](slides/cloudformation.png) CloudFormation

AWS infrastructure templates

Note: The first two tools focused on automating servers and
server-like objects (containers). When we looked at Lambda, we saw how
we could do some powerful automation by hooking events from one
service into the trigger of another service. This is a common pattern
in the cloud - many services connected together to accomplish a larger
goal. CloudFormation is designed to provision and configure multiple
services together as a unit, with a single template that can be
managed.

---

<!-- .slide: data-background-image="slides/cloudformation.png" -->

`bucket.yml`

```
---
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  BucketName:
    Type: String
    Default: my-awesome-bucket

Resources:
  StaticBucket:
    Type: "AWS::S3::Bucket"
    Properties:
      BucketName: !Ref BucketName
```

Note: If you're just getting started with CloudFormation, start with
something as simple as this. This template only creates an S3 bucket,
which doesn't sound exciting, but you can pretty quickly build on this
for your own use case.

---

<!-- .slide: data-background-image="slides/cloudformation.png" -->

`whatismyip.yml`

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: "AWS::Serverless-2016-10-31"
Resources:
  WhatIsMyIP:
    Type: "AWS::Serverless::Function"
    Properties:
      Handler: index.handler
      Runtime: python3.7
      InlineCode: |
        import json
        def handler(event, context):
          body = {'ip': event['requestContext']['identity']['sourceIp']}
          return {'statusCode': '200', 'body': json.dumps(body)}
      Events:
        Web:
          Type: Api
          Properties:
            Path: /
            Method: get
```
<!-- .element: class="yaml medium" -->

---

<!-- .slide: data-background-image="slides/cloudformation.png" -->

`aws cloudformation create-stack`

`--stack-name whatismyip --template-body file://whatismyip.yml`<br>`--capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM`
<!-- .element: style="font-size:60%" -->

<iframe data-src="/wetty" width="100%" height="400px"></iframe>

Note: CloudFormation is a very powerful tool. Nearly every AWS service
is supported by CloudFormation, and you can even create custom
resources powered by Lambda which can do some amazing things.

---

<!-- .slide: data-background-image="slides/cloudformation.png" class="get-started" -->

### Get Started

* [docs.aws.amazon.com/AWSCloudFormation/latest/<wbr>UserGuide/gettingstarted.templatebasics.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html)
* [aws.amazon.com/serverless/sam](https://aws.amazon.com/serverless/sam/)

---

<!-- .slide: data-background="#286ee0" -->
## Thanks!

![bioteam](slides/bioteam-wt.png)<br>
&#x2b91; [bioteam.net](https://bioteam.net)
