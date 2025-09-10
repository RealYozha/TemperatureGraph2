# Temperature Graph 2

![`v1.2.1`](https://img.shields.io/badge/version-1.2.1-green)
![`latest release: stable`](https://img.shields.io/badge/latest_release-stable-lime)

A program fully written in Python, shows a temperature graph via APIs.

## Installation

Firstly, install python 3 and pip.
Secondly, download the source code.
Then, run the following commands in your terminal:

For Windows:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

For Linux/MacOS:

```bash
python -m venv .venv
./.venv/bin/activate
pip install -r requirements.txt
```

After you've done this, create a `.env` file and paste this in there:

```env
YANDEX_GEOCODER_APIKEY=
```

where after the  `=` comes your Yandex Geocoder api key.

Then, edit these variables in `main.py`:

```python
city_name = "YOUR CITY NAME HERE"
start_date = "YYYY-MM-DD"
end_date = "YYYY-MM-DD"
```

## Running

To run the program, run this command:

```bash
> python main.py
```

## Result

A window with a graph will open, featuring temperature of your desired city set in `main.py`.
