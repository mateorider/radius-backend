# radius Backend

## Setup
1. Follow this wiki page to get [dependencies installed][dependencies_installed]

[dependencies_installed]: https://github.com/dwbelliston/radius-backend/wiki/Dependencies-install

1. Follow this wiki page to get [virtualenv setup][virtualenv]

[virtualenv]: https://github.com/dwbelliston/radius-backend/wiki/Virtualenv

    _(Note: make certain you are using **python3** for this - python2 is no longer supported, and will not work!)_

1. Create the database:

    _Mac users_ - use brew to start postgres before creating the database

    ```bash
    brew services start postgres
    brew services stop postgres
    ```

    If first time logging into postgres, create the default db

    ```bash
    createdb `whoami`
    ````

    ```bash
    psql
    psql# CREATE USER radius WITH PASSWORD 'radius';
    psql# CREATE DATABASE radius_dev OWNER radius;
    psql# ALTER USER radius CREATEDB;
    ```  

1. Migrate the database:

    Go to the project root for this command

    ```bash
    ./manage.py migrate
    ```

    Sometimes you will need to make migrations when you make changes to the models. This generates sql steps that will be placed in a migration file. Those are pushed up with your commit and the next dev can run those migrations on their database.

    ```bash
    ./manage.py make-migrations
    ```

1. Create a superuser to access the admin:

    ```bash
    ./manage.py createsuperuser
    ```

1. Start a locally-accessible development webserver:

    ```bash
    ./manage.py runserver 0.0.0.0:8000
    ```

You should have a live project running at :8000

**Admin/API**

Visit the admin in your browser at: [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)

Visit the api in your browser at: [http://0.0.0.0:8000/api](http://0.0.0.0:8000/api)

-----

Check out this wiki page to view [Common development tasks][cmtask]

[cmtask]: https://github.com/dwbelliston/radius-backend/wiki/Common-development-tasks
"# radius-backend"
