# EC2 instance auto-tag Lambda function

## Prerequisites

You need to have a CloudTrail trail created in order to process these
events.

1. Open the CloudTrail console and click "View trails"
2. If there exists a trail which writes to a bucket that you can read,
   then proceed with the Lambda setup. Otherwise, click "Create
   trail".
    * Put anything in Trail name
    * "Apply trail to all regions" can be either yes or no
    * Under Management events, select "All" for Read/Write events
    * Don't specify any data events
    * Create a new S3 bucket, named "cloudtrail-ACCOUNTID" where
      ACCOUNTID is your twelve-digit account number

## Setup

1. Open the Lambda console and create a new function
    * Choose "author from scratch"
    * Enter "auto-tag-instances" as the function name
    * Select "Python 3.7" as the runtime
    * In the Permissions section, choose "Create a new role with basic
      Lambda permissions"

2. In the Designer section, add a new "CloudWatch Events" trigger.
   Scroll down to configure it.
    * Choose "Create a new rule"
    * Name it "detect-instance-launch"
    * Set the rule type to "Event pattern"
    * Choose EC2 from the first dropdown, and "AWS API Call via
      CloudTrail" from the second
    * Enable Operation detail and specify "RunInstances" in the box
    * Click "Add"
    
3. Copy the code from `autotag.py` into the Lambda function code pane.
   You may need to click on the Lambda icon in the center of the
   "Designer" window to bring up the code editor.
   
4. Once entered, click Save in the upper right

5. The newly created Lambda function role needs to be granted
   additional permissions to be able to tag EC2 instances. Open the
   IAM console and select "Roles".
    * Search for and open the "auto-tag-instances-role-xxxxxxxx"
    * Click "Add inline policy" at the right of the page above the list
      of policies
    * Using the Visual editor:
        * Select the EC2 service
        * Type "tag" in the "Filter actions" box and select "CreateTags" 
        * In the Resources section, choose All resources
        * Click "Review policy"
        * Name the policy "TagInstances" and save
        
6. Test the new automation by launching an instance and seeing if the
   tag is automatically applied. Note that it may take several minutes
   for the event to propagate through CloudTrail.
