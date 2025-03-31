# IntelliStar-Like Weather Dashboard

This project aims to create a weather dashboard with a similar look and feel to The Weather Channel's IntelliStar units. The dashboard displays current weather conditions, forecasts, radar maps, and alerts.

## Features

- **Current Weather**: Displays the current temperature, weather conditions, humidity, and wind speed.
- **Forecast**: Shows multi-day weather forecasts.
- **Radar Maps**: Displays weather radar images.
- **Alerts**: Shows weather alerts and warnings.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- Requests library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/G34hWeatherSpotter/intellistar-weather-dashboard.git
    cd intellistar-weather-dashboard
    ```

2. Install the required Python packages:
    ```bash
    pip3 install flask requests
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'your_openweathermap_api_key'` in the `fetch_weather_data.py` and `weather_dashboard_web.py` files with your API key.

### Running the Dashboard

1. Run the Flask application:
    ```bash
    python3 weather_dashboard_web.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to view the dashboard.

## Project Structure

- `fetch_weather_data.py`: Script to fetch weather data from OpenWeatherMap.
- `weather_dashboard_web.py`: Flask application to serve the weather dashboard.
- `templates/index.html`: HTML template for the dashboard.
- `static/styles.css`: CSS file for styling the dashboard.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
