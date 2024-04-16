---
date: 2024-04-16T09:40:24.887393
author: AutoGPT <info@agpt.co>
---

# xkcd

Following our earlier conversation, the requirement is for an endpoint that returns only the latest XKCD comic. Implementing this feature involves using the tech stack specified: Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. The endpoint can be designed to fetch the latest comic's information from the XKCD API endpoint (`https://xkcd.com/info.0.json`), parse its content, and then serve it to the user in a JSON format structured according to the project's data models. This endpoint will be a valuable addition for users looking to get quick and updated access to the latest XKCD comics.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'xkcd'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
