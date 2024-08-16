# Use the specified PostGIS image as the base image
FROM kartoza/postgis:9.6-2.4

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=user001
ENV POSTGRES_PASSWORD=123456789
ENV POSTGRES_DBNAME=gis

# Expose the PostgreSQL port
EXPOSE 5432


# Build the image: docker build -t custom_postgis_image .
# Run the container: docker run --name=postgis -d -p 5432:5432 custom_postgis_image
