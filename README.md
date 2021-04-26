# Google Pages Speed

The goal of this project is to retrieve metrics from pageSpeed and save the results to a sqlite database.

To do this, a docker container was created with Python and sqlite.
Once the project is started, it is possible to take the list of urls and store the results in a table in the db.

The chosen metric was lighthouseResult > performance > score.


## How it works

### Initial settings

#### Define your `API_KEY`:

1. Rename the file `__init__.bak` locateted in the `src/config` folder to `__init__.py`.
2. Go to this [link](https://developers.google.com/speed/docs/insights/v5/get-started) and get your `API_KEY`.
3. Set the value in the constant `API_KEY` defined in the file `__init__.py`.

#### Prepare your data:

Prepare the list of urls in the `.csv` file located in the `data` folder as shown in the example.
You can update the list as many times as you want.

### Run the app:
The first time the project is used, the following commands should be run:

1. Build container:
`docker-compose build`

2. Run Script
`docker-compose run server python src/app.py`

3. To shut down container:
`docker-compose down`


### Get dB
To get the result just copy the file `database.db` located in the `results`folder.


## Additional Information

#### Stack
- Docker
- Docker Compose
- Python
- SQLite
- Pandas

#### Dependencies
- https://developers.google.com/speed/docs/insights/v5/get-started
- https://pypi.org/project/requests/
- https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html