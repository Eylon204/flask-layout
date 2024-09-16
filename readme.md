# Flask Web Application

## Overview

This is a simple Flask web application that uses Jinja2 templates to structure and serve different pages like the homepage and an about page. It includes CSS styling for layout and navigation.

## Files

### 1. `app.py`
This is the main application file where the Flask application is initialized, routes are defined, and the server is started.

### 2. `layout.html`
This is the base template for the web pages. It includes the structure for the HTML head and body, as well as a navigation bar. Other templates extend from this layout to create uniformity across the website.

Key Features:
- **CSS for navigation bar**: A simple navigation bar styled with CSS.
- **Dynamic content blocks**: Jinja2 blocks (`head`, `title`, `content`, `footer`) are used to dynamically insert content for different pages.

### 3. `about.html`
This is the "About" page of the web application. It extends `layout.html` and provides content specific to the About section.

Key Features:
- **Page Title**: `about`
- **Custom CSS class**: `.important` is defined to style important text with a custom color (`#336699`).
- **Content**: Contains a heading and a paragraph introducing the "About" section.

### 4. `main.html`
This is the homepage of the web application. Similar to `about.html`, it extends `layout.html` and inserts content into the defined blocks.

Key Features:
- **Page Title**: `Index`
- **Custom CSS class**: `.important` is reused here to style the welcome message.
- **Content**: Displays a welcoming message for the homepage.

### 5. `style.css` (referenced in `layout.html`)
This CSS file is linked to the templates via `{{ url_for('static', filename='style.css') }}`. It styles various aspects of the webpage, including layout, text, and background colors.

### 6. `mylog.txt`
A simple log or note file that contains tasks or future goals for the project (e.g., "to do...").

## Setup Instructions

## 1. Install Dependencies:  
   Install Flask if you don’t already have it:
   pip install Flask

##   2.	Run the App:
    python app.py

##  3.	Access the Website:
    Open a browser and navigate to http://127.0.0.1:5000/ to view the homepage.

# Project Structure:
/project-directory
│
├── app.py               # Main Flask app
├── templates/           # Directory containing HTML files
│   ├── layout.html      # Base layout file
│   ├── about.html       # About page
│   ├── main.html        # Homepage
├── static/              # Directory containing static files (CSS, JS, etc.)
│   ├── style.css        # CSS file for styling
├── mylog.txt            # Log file with to-do tasks
└── README.md            # This file

# Future Enhancements

	•	Add more pages with similar styling.
	•	Implement user authentication and dynamic content loading.
	•	Improve the CSS for a more modern design.