import os
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from schemas.request import Request
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

# Preprocessing data
df = pd.read_csv("ADANIPORTS.csv")
columns = ["Date", "Close"]
df = df[columns]
df["Date"] = pd.to_datetime(df["Date"])

api = APIRouter()


def save_file(x: list, y: list):
    """
    Name: Save File
    Parameters: x: list, y: list
    Description: Function to plot the graph and save it to the file system
    """

    plt = sns.lineplot(x=x, y=y)
    plt.set_title("ADANIPORTS")
    plt.set_xlabel("Date")
    plt.set_ylabel("Closing Price")
    plt.figure.tight_layout()
    plt.figure.autofmt_xdate()
    plt.figure.savefig("graph.png")


def remove_file(path: str):
    """
    Name: Remove File
    Parameters: path: str
    Description: Function to remove the file from the file system
    """

    os.remove(path)


@api.get("/")
def read_root():
    """
    Name: Root
    Method: GET
    Description: This is the root of the API
    """

    return JSONResponse(
        content={
            "code": 200,
            "message": "success",
            "data": {
                "endpoints": [
                    {
                        "url": "/",
                        "method": "GET",
                        "description": "Root",
                        "example": "http://localhost:8000/api/",
                    },
                    {
                        "url": "/graph",
                        "method": "POST",
                        "description": "Graph",
                        "parameters": [
                            {"name": "start", "type": "str", "required": True},
                            {"name": "end", "type": "str", "required": True},
                        ],
                        "example": "http://localhost:8000/api/graph?start=2007-11-27&end=2021-04-30",
                    },
                ],
                "Description": "PineLabs task",
                "Contact": "Kapil Nallathambi: kapil.nallathambi@pinelabs.com",
            },
        }
    )


@api.get("/graph")
def graph(start: str, end: str, background_tasks: BackgroundTasks):
    """
    Name: Graph
    Method: GET
    Parameters: start: str, end: str
    Description: This endpoint returns a graph of the closing price for the given date range
    """

    try:
        start_date = pd.to_datetime(start)
        end_date = pd.to_datetime(end)

        # Filter the dataframe based on the date range
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            return JSONResponse(
                content={
                    "code": 404,
                    "message": "No data found",
                    "data": "No data found",
                }
            )

        filtered_df.loc[:, "Date"] = filtered_df["Date"].astype(str)

        # Convert the dataframe to a 2D numpy array
        data = filtered_df.to_numpy()

        #  Example data
        #  [
        #    [Timestamp('2007-12-24 00:00:00'), 1156.8],
        #    [Timestamp('2007-12-20 00:00:00'), 1060.2],
        #    [Timestamp('2007-12-26 00:00:00'), 1199.9],
        #    [Timestamp('2007-12-27 00:00:00'), 1211.65]
        #  ]

        save_file(data[:, 0], data[:, 1])

        # Remove the file from the file system after the response is sent
        background_tasks.add_task(remove_file, "graph.png")

        return FileResponse("graph.png", media_type="image/png")

    except Exception as e:
        raise JSONResponse(
            content={
                "code": 500,
                "message": "Internal Server Error",
                "error": str(e),
            }
        )
