## cornershop-backend-test


### Running the development environment

* `make up`
* `dev up`

##### Install users and nora
#####Creation of nora whit permissions and employees
* `sh backend_test/utils/install_users.sh`

##### Project documentations, open on browser
[https://donovan-vargas.github.io/cornershopt-test-docs/](https://donovan-vargas.github.io/cornershopt-test-docs/)
#####or
* `docs/_build/html/index.html`
##### settings variables settings.py 
* `SLACK_CHANNEL` slack channel to send menus
* `SLACK_OAUTH_ACCESS_TOKEN` slack bot token
* `LIMIT_HOUR` Limit hour to request a menu orders option default set on 11 am
* `MENU_CREATE_HOUR` limit hour to create a new today menu option default set on 8 am
* `EMPLOYEES_TIME_ZONE` employees time zone set on santiago chile
* `LOCAL_SITE` to send url menu default set http://0.0.0.0:8000/menu/
##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000

####Login
* Local: http://127.0.0.1:8000/login
#####As nora:
#####username: nora password: 123456
#####As employee (employee_0 to employee_9):
#####username: employee_0 password: 123456
####Logut
* Local: http://127.0.0.1:8000/logout
####Create new menu (login required permission required 'menu.can_create_menu')
* Local: http://127.0.0.1:8000/menu/add/
####Edit menu (login required permission required 'menu.can_edit_menu')
* Local: http://127.0.0.1:8000/menu/update/<int:pk>/
####Today menu and options
* Local: http://127.0.0.1:8000/menu/<uuid:unique_id>/
####Request menu option (login required)
* Local: http://127.0.0.1:8000/menu/<uuid:unique_id>/
####List orders (login required)
* Local: http://127.0.0.1:8000/orders-list/
