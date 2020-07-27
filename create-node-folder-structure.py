import sys
import os

def CreatingStructure(projectName):
  os.mkdir(projectName)

  os.chdir(projectName)
  os.mknod("Dockerfile")
  os.mknod("README.md")
  os.mknod(".env")
  os.mkdir("src")

  os.chdir("src")
  os.mknod("app.js")
  os.mknod("server.js")
  os.mkdir("api")
  os.mkdir("config")
  os.mkdir("database")
  os.mkdir("services")
  os.mkdir("tests")

  os.chdir("config")
  os.mknod("routes.js")
  os.mknod("environment.js")
  os.mknod("dbConnection.js")

  os.chdir("../database")
  os.mknod("connection.js")
  os.mkdir("migrations")
  os.mkdir("models")

  os.chdir("../tests")
  os.mkdir("unit")
  os.mkdir("integration")

def LogNextSteps(projectName):
  print(f"Files and Folders of {projectName} have been created!")
  print("-> Run npm init or yarn init in the project's root directory")
  print("-> Run git init in the project's root directory if you intend to use git")

def main(projectName):
  try:
    CreatingStructure(projectName)
    LogNextSteps(projectName)
  except Exception as err:
    print("Something went wrong!")
    print(err)


if __name__ == "__main__":
  main(sys.argv[1])