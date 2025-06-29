# Dockerizing GeoDjango with Postgres, Gunicorn, and Nginx

## Want to learn how to build this?

## Want to use this project?

### Docker Configuration

This project includes Docker configuration for both development and production environments:

- **Development**: Uses the Django development server with a PostgreSQL database.
- **Production**: Uses Gunicorn, Nginx, and PostgreSQL with PostGIS for a production-ready setup.

The Dockerfile includes all necessary dependencies for GeoDjango, including GDAL, PROJ, and other spatial libraries.

### Features

This project includes a Location model with GIS capabilities:

- Store geographical points with name and description
- RESTful API for CRUD operations on locations
- Admin interface for managing locations
- Sample data loading script

### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml* and *.env* files if needed.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "GeoDjangoDocker" folder is mounted into the container and your code changes apply automatically.

1. Load sample location data (choose one of the following methods):

    Using the custom management command:
    ```sh
    $ docker-compose exec web python manage.py add_sample_locations
    ```

    Or using the fixture:
    ```sh
    $ docker-compose exec web python manage.py loaddata sample_locations
    ```

    This will add several famous landmarks with their geographical coordinates to the database.

1. Access the API at [http://localhost:8000/api/locations/](http://localhost:8000/api/locations/) to see the location data.

1. Access the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage locations.

### Production

Uses gunicorn + nginx.

1. Update the environment variables in the *.env.prod* and *.env.prod.db* files if needed.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

1. Collect static files:

    ```sh
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    ```

1. Load sample location data (choose one of the following methods):

    Using the custom management command:
    ```sh
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py add_sample_locations
    ```

    Or using the fixture:
    ```sh
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py loaddata sample_locations
    ```

1. Access the API at [http://localhost:1337/api/locations/](http://localhost:1337/api/locations/) to see the location data.

1. Access the admin interface at [http://localhost:1337/admin/](http://localhost:1337/admin/) to manage locations.
