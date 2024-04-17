### System Monitoring Web Application

This Python project is a web-based system monitoring application built with Flask. It's designed to display the current CPU and memory usage of your system through a user-friendly dashboard interface. The application fetches real-time statistics and presents them to the user via a JSON response on a dedicated stats page.

#### Features
- **Home Page:** A landing page that can be customized with HTML and CSS.
- **Real-Time Stats:** Dynamic fetching of CPU and memory usage stats, available via a `/stats` endpoint.
- **JSON API:** The stats page provides a JSON response with current CPU and memory usage, which can be used for integration with other applications or for remote monitoring.
- **HTML Template Rendering:** Utilizes Flask's `render_template` function to serve HTML content for the home page.

#### Structure
- `app.py`: The main Flask application script.
- `dashboard.py`: A separate module that contains functions like `cpu_usage()` and `memory_usage()` to get system statistics.
- `static/`: A directory for static files such as CSS, JavaScript, and images that style the web interface.
- `templates/`: A directory containing HTML templates for the Flask app.

#### How to Use
1. **Run the App:** Execute the `app.py` script to start the Flask server.
2. **Visit Home Page:** Access the home page by navigating to the root URL (`/`) in your web browser.
3. **View Stats:** Go to the `/stats` URL to see real-time CPU and memory usage data in JSON format.

#### Requirements
- Python 3.x
- Flask (`pip install flask`)
- Functions for `cpu_usage()` and `memory_usage()` (presumably provided in `dashboard.py`)

The app can be used for monitoring the resource usage of a server or local machine, making it a useful tool for system administrators and developers. With a front-end designed using HTML and CSS, users can enjoy a visually appealing and informative experience.

If you have HTML and CSS files ready, they can be placed within the `templates` and `static` directories, respectively, to customize the appearance and layout of your application's interface.
