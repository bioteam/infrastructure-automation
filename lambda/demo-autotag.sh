#!/bin/bash

clear

# Launch an EC2 instance purely for the purpose of testing the
# auto-tagging functionality. This instance will launch in the default
# VPC with default security groups and no key pair, so it is
# effectively useless - however, we will terminate it automatically
# when the script exits.

echo Launching EC2 instance ...

instance_id=$(aws ec2 run-instances \
                  --image-id ami-0de53d8956e8dcf80 \
                  --instance-type t2.micro \
                  --query 'Instances[*].InstanceId' --output text)
echo Instance ID: $instance_id
echo

teardown() {
    echo
    echo
    echo Terminating EC2 instance ...
    aws ec2 terminate-instances --instance-ids $instance_id --output text
}

trap teardown EXIT

sleep 1
echo "Watching instance state (Ctrl-C to abort) ..."
echo "Current time                 Instance ID         Launch time              State   Tags"
echo "--------------------------------------------------------------------------------------------"

while sleep 1; do
    state=$(aws ec2 describe-instances \
                --filter "Name=instance-id,Values=${instance_id}" \
                --query 'Reservations[*].Instances[*].[InstanceId,LaunchTime,State.Name,Tags]'\
                --output text 2>/dev/null)
    echo -n $(date) $state $'\r'
done

