# Movie-Stat 
Allow us to run the and do the data analysis on movie stat

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Deep9968/Movies-Stat
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Run `main.py` to create tables in the database:

    ```bash
    python main.py
    ```

   This step initializes the necessary database tables.

2. `main.py` will use queries in `query.py` to interact with the created tables:







