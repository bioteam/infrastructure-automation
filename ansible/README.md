
# Quickstart

To run this code on your local system:

    $ pip install ansible
    $ ansible-playbook webserver.yml
    
## Remote management

To run it against a remote system, create a file named `hosts` with
your desired destination hostname, edit the desired playbook and
replace the line `hosts: localhost` with `hosts: your_host_name`, and
then run the command:

    $ ansible-playbook -i hosts database.yml
    
If you are connecting to the remote server using your own username and
password, you will need to add `--sudo` to the command options.

## Variables

You can set values of variables by adding `-e variable_name=value` to
the command line. For example, the `database.yml` template uses the
`pg_sync` variable to enable or disable synchronous commit. The
command

    $ ansible-playbook -e pg_sync=off database.yml
    
will disable synchronous commit and restart the database.

