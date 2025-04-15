# nginx/Dockerfile (create an 'nginx' subdirectory and place this file inside)

# Use the official Nginx image
FROM nginx:stable-alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom configuration file from the context to the container
COPY nginx.conf /etc/nginx/conf.d/