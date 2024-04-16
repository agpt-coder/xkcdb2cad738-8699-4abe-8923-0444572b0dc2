import httpx
import prisma
import prisma.models
from pydantic import BaseModel


class LatestComicResponse(BaseModel):
    """
    Response model containing the latest XKCD comic's information, including ID, title, URL, image URL, publication date, and alt text.
    """

    id: int
    num: int
    title: str
    img: str
    alt: str
    day: str
    month: str
    year: str


async def get_latest_comic() -> LatestComicResponse:
    """
    Fetches the latest XKCD comic information.

    Args:


    Returns:
    LatestComicResponse: Response model containing the latest XKCD comic's information, including ID, title, URL, image URL, publication date, and alt text.
    """
    url = "https://xkcd.com/info.0.json"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        comic_data = resp.json()
    comic_id = comic_data["num"]
    comic_exists = await prisma.models.Comic.prisma().find_unique(
        where={"num": comic_id}
    )
    if not comic_exists:
        new_comic = await prisma.models.Comic.prisma().create(
            data={
                "num": comic_id,
                "title": comic_data["title"],
                "img": comic_data["img"],
                "alt": comic_data["alt"],
                "day": comic_data["day"],
                "month": comic_data["month"],
                "year": comic_data["year"],
            }
        )
        comic_exists = new_comic
    return LatestComicResponse(
        id=comic_exists.id,
        num=comic_exists.num,
        title=comic_exists.title,
        img=comic_exists.img,
        alt=comic_exists.alt,
        day=comic_exists.day,
        month=comic_exists.month,
        year=comic_exists.year,
    )
