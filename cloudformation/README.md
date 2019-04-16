# Launching

These templates can all be launched via the
AWS [CloudFormation console][1] or via the command line.

[1]: https://console.aws.amazon.com/cloudformation/home

## Via the console

1. Log in to the main AWS console and type "cloudformation" into the
   search bar.
   
2. Click "Create stack"

3. Choose "Upload a template file" and upload your desired template.
   Click "Next".
   
4. Enter any stack name and fill in any required parameters. Click
   "Next".
   
5. Leave all stack options as their defaults. Click "Next".

   NOTE: For troubleshooting a stack that is failing to launch, you
   may wish to disable "rollback on failure" within the Stack creation
   options.
   
6. Scroll to the bottom of the stack review screen. Acknowledge any
   capabilities required by the stack, then click "Create stack".
   
7. Watch the stack as it is created by periodically refreshing the
   Events view. When the stack reaches "CREATE_COMPLETE" state, any
   outputs should be visible in the Outputs tab.
   
8. When you are ready to be done with the stack, select "Delete stack"
   from the Actions menu.
   
## Via the command line

You will need to first have the AWS CLI installed, which is most
easily done with the command `pip install awscli`. For Windows
instructions and more details, see
the [AWS CLI page](https://aws.amazon.com/cli/).

The simple `bucket.yml` and `webserver.yml` templates can be launched
with a simple command line:

    $ aws cloudformation create-stack --stack-name my-bucket --template-body file://bucket.yml

The `bucket.yml` template parameter BucketName can be overridden by
adding a parameter to the command line:

    --parameters ParameterName=BucketName,ParameterValue=my-new-value

The `whatismyip.yml` template uses features which require
acknowledging certain capabilities of CloudFormation. In addition to
the base `create-stack` command line above, the `--capabilities`
parameter and its arguments needs to be added:

    --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
    
