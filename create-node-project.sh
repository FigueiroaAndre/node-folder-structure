mkdir $1

cd $1
touch Dockerfile
touch README.md
touch .env
mkdir src

cd src
touch app.js
touch server.js
mkdir api
mkdir config
mkdir database
mkdir services
mkdir tests

cd database
mkdir models
mkdir migrations
touch connections.js

cd ../tests
mkdir unit
mkdir integration

echo "Files and Folders created"
echo "Next steps:"
echo "-> Enter the project directory"
echo "-> Run npm init or yarn init"
echo "-> Run git init if you intend to use git"