
## Setup

MediaWiki has an online setup process which needs to be run before use.

1. Run this stack with `docker-compose up`. Be sure that the line
   referencing `LocalSettings.php` is commented out.
   
2. Open `http://localhost:8080` in your browser and begin the setup
   process.
   
3. When prompted for database information, provide the following:

    * MariaDB type
    * Host: `database`
    * Database name: `my_wiki`
    * No database table prefix
    * Database username: `wikiuser`
    * Database password: `example`
    * InnoDB storage engine
    
4. Provide a name for the wiki and an administrator username and password.

5. Complete the installation and ensure that the `LocalSettings.php`
   file has been downloaded to your computer.

6. Ctrl-C the running `docker-compose` session.

7. Place `LocalSettings.php` in this directory, and edit
   `docker-compose.yml` to remove the commented out line referencing
   `LocalSettings.php` in the `volumes:` section.
   
8. Run `docker-compose up` again.
