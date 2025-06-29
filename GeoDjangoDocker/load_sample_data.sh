#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Run the Django management command to add sample locations
echo "Adding sample location data..."
python manage.py add_sample_locations

echo "Done! Sample location data has been added to the database."
echo "You can now access the data through the API at: http://localhost:8000/api/locations/"
echo "Or through the Django admin interface at: http://localhost:8000/admin/"