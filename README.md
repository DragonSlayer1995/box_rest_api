#### 1. Create and activate venv if you don't

#### 2. Install requirements.txt - `pip install -r requirements.txt`

#### 3. Run flask application
- Set app name - `set FLASK_APP=app.main`
- Run flask - `flask run`

#### 4. Run tests - `pytest`

#### Additional: You can run tests by markers
- Positive - `pytest -m positive`
- Negative - `pytest -m negative`
- Validation - `pytest -m validation`
- End2End - `pytest -m e2e`
 
You can find more about markers in `pytest.ini` file
