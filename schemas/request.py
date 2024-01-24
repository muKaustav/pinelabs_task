from pydantic import BaseModel


class Request(BaseModel):
    """
    Name: Request
    Description: Base request model
    """

    start: str
    end: str
