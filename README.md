<h1 align="center">PineLabs API 📊</h1>

## Overview

- This API provides a simple interface for visualizing time-series data.
- Built using Python and FastAPI.
- The system uses data stored in a csv file, which is read and processed by the API.
- ADANIPORTS stock data is used, which is available on [NIFTY-50 Stock Market Data (2000 - 2021)](https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data).
- The API is deployed on an AWS EC2 instance, and can be accessed at http://3.110.30.132:8000/api/.

## Getting Started

- Clone the repository.
- Create a virtual environment using `python -m venv env`.
- Activate the virtual environment using `source env/bin/activate`.
- Install the required dependencies using `pip install -r requirements.txt`.
- Run the API using uvicorn `uvicorn server:app --host 0.0.0.0 --port 8000`.
- Access the API documentation at http://localhost:8000/docs.

## Routes

### 1. Root

- **Method**: GET
- **Endpoint**: `/`
- **Description**: This is the root of the API, providing information about available endpoints and contact details.
- **Example Request**: http://3.110.30.132:8000/api/
- **Example Response**:

```json
{
	"code": 200,
	"message": "success",
	"data": {
		"endpoints": [
			{
				"url": "/",
				"method": "GET",
				"description": "Root",
				"example": "/"
			},
			{
				"url": "/graph",
				"method": "GET",
				"description": "Graph",
				"parameters": [
					{ "name": "start", "type": "str", "required": true },
					{ "name": "end", "type": "str", "required": true }
				],
				"example": "/graph?start=2007-11-27&end=2021-04-30"
			}
		],
		"Description": "PineLabs task: Data Visualization API",
		"Contact": "Your Name: your.email@example.com"
	}
}
```

### 2. Graph

- **Method**: GET
- **Endpoint**: `graph`
- **Description**: This endpoint returns a graph of the closing price for the given date range.
- **Parameters**:

```
start (str): Start date in the format "YYYY-MM-DD".
end (str): End date in the format "YYYY-MM-DD".
```

- **Example Request**: http://3.110.30.132:8000/api/graph?start=2007-11-27&end=2021-04-30
- **Example Response**:

<p align = center>
    <img alt="Project Logo" src="https://raw.githubusercontent.com/muKaustav/pinelabs_task/main/assets/graph.png" target="_blank" />
</p>

## Author

**Kaustav Mukhopadhyay**

- Linkedin: [@kaustavmukhopadhyay](https://www.linkedin.com/in/kaustavmukhopadhyay/)
- Github: [@muKaustav](https://github.com/muKaustav)

<br/>

---
