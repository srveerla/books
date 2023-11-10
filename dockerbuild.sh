cd books
sudo podman build -t books-service .
sudo podman tag localhost/books-service srveerla/books-service:latest
sudo podman push srveerla/books-service:latest
cd ../users/
sudo podman build -t users-service .
sudo podman tag localhost/users-service srveerla/users-service:latest
sudo podman push srveerla/users-service:latest
cd ../renting/
sudo podman build -t renting-service .
sudo podman tag localhost/renting-service srveerla/renting-service:latest
sudo podman push srveerla/renting-service:latest
