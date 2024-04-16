import logging
from contextlib import asynccontextmanager

import project.get_latest_comic_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="xkcd",
    lifespan=lifespan,
    description="Following our earlier conversation, the requirement is for an endpoint that returns only the latest XKCD comic. Implementing this feature involves using the tech stack specified: Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. The endpoint can be designed to fetch the latest comic's information from the XKCD API endpoint (`https://xkcd.com/info.0.json`), parse its content, and then serve it to the user in a JSON format structured according to the project's data models. This endpoint will be a valuable addition for users looking to get quick and updated access to the latest XKCD comics.",
)


@app.get(
    "/comics/latest",
    response_model=project.get_latest_comic_service.LatestComicResponse,
)
async def api_get_get_latest_comic() -> project.get_latest_comic_service.LatestComicResponse | Response:
    """
    Fetches the latest XKCD comic information.
    """
    try:
        res = await project.get_latest_comic_service.get_latest_comic()
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
