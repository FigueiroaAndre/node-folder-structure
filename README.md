# Node Folder Structure
Folder and file structure for quick starting node.js REST API applications. The structure might be updated in the future.

version: 1.0.0

## Step by step

1- run create-node-folder-structure.py in the directory you want to create your project and pass the project name as argument.
```
python3 create-node-folder-structure.py my-project-name
```
If it does not work, try run it with `sudo`

2- run `npm init or yarn init`

3- run `git init` if you intend to use git

## Folder Structure

📄 Dockerfile

📄 README.md

📄 .env

📁 src `application's source files`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 app.js `express configuration`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 server.js `server`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 api `contain route controllers for api endpoints (e.g: http related code)`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 config `environment variables and other configuration files`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 routes.js `configuration of the routes of your application`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 environment.js `importing environment variables to the project`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 dbConnection.js `database connection configuration`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 database

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 connection.js `database connection`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 models `database models`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 migrations `database migrations`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 services `business logic (e.g: interacting with sequelize for CRUD operations)`

&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 tests

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 unit

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 📁 integration
