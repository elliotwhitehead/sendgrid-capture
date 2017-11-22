## Installation
1. Create a [python3 virtual environment](https://virtualenv.pypa.io/en/stable/reference/#cmdoption-p)
2. Install requirements: `pip install -r requirements.txt`
3. `export FLASK_APP=app.py`
4. Set your Sendgrid api key environment variable: `export SENDGRID_API_KEY=<your-api-key-here>`
    * Steps 3 & 4 must be repeated each time you start a new terminal session, as they're just environment variables
5. `flask run`
