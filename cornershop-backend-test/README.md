## cornershop-backend-test


### Running the development environment

* `make up`
* `dev up`

##### Install users and nora
######Creation of nora and employees
* `sh backend_test/utils/install_users.sh`

##### Project documentations open on browser
* `docs/_build/html/index.html`

##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000

####For login
* Local: http://127.0.0.1:8000/login
#####As nora:
######username: nora password: 123456
#####As employee (employee_0 to employee_9):
######username: employee_0 password: 123456