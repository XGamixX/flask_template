# Flask Template

This is a template for hosting simple web-services using Python Flask in a Docker container

## Usage

1. Create a new Repository using this template
2. Change Workflow permissions of the Repository to have read and write permissions (in `Settings -> Code and automation -> Actions -> General`)
3. Edit the name of the container in `docker-compose.yaml` and the `IMAGE_NAME` in `.github/workflows/docker-image.yml`

- When adding the first html template or static file (in the `templates` or `static` folder) uncomment the respective folder in the `Dockerfile`