# Web Scraping USA States Data

This project aims to extract data about the states of the United States of America (USA) from the Wikipedia page [List of states and territories of the United States](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States) using Python and BeautifulSoup library, and create csv file.

## Table of Contents

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Extracted](#data-extracted)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Web scraping is the process of extracting data from websites. In this project, we scrape data from the Wikipedia page [List of states and territories of the United States](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States), which contains a table with information about USA states such as their name, abbreviation, capital, population, and area.

Also used the BeautifulSoup library in Python to parse the HTML content of the webpage and extract the desired data.

csv library in Python to create csv file of the extracted data

## Dependencies

- Python 3.x
- BeautifulSoup4 (bs4)
- Requests
- csv

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/web-scraping-usa-states.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install beautifulsoup4
    pip install requests
    pip install csv
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd web-scraping-usa-states
    ```

2. Run the Python script `scrape_usa_states.py`:

    ```bash
    python scrape_usa_states.py
    ```

3. The script will scrape the data from the Wikipedia page and print the extracted information.

## Data Extracted

The following data is extracted for each state:

- State Name
- Postal Abbreviations
- Capital
- Largest	
- Ratification Or Admission
- Population
- Total Area In MiÂ²
- Total Area In KmÂ²
- Number Of Representatives

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Wikipedia Page Link

You can find the Wikipedia page [here](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States).
