# 🎮 Nintendo Deals

A personal project built to strengthen my skills in **Web Scraping**, **REST API development**, **Python web applications**, and **data visualization** by creating a Nintendo game price comparison platform.

The idea behind this project is to simulate a real-world data pipeline:

> Collect data → Process it → Expose it through an API → Consume it with a web application.

Rather than focusing only on the frontend, this project demonstrates the complete lifecycle of working with data.

---

## 🚀 Project Overview

Nintendo Deals is composed of two independent applications:

### 🔹 Data API
Responsible for collecting and exposing Nintendo game information.

Main responsibilities:

- Web scraping product information
- Data normalization
- REST API development using Flask
- JSON serialization
- Deployment on Vercel

Current API endpoint:

```
https://flask-api-videogames.vercel.app/products
```

---

### 🔹 Web Application

A Flask web application that consumes the REST API and displays Nintendo products in a modern catalog interface.

Current features include:

- Product catalog
- Product detail page
- Search functionality
- Category filtering
- Responsive design
- External links to original stores

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- Requests

## Frontend

- HTML5
- CSS3
- JavaScript

## Deployment

- Vercel

## Data Source

- Web Scraping

---

# 📂 Project Structure

```
nintendo-games-web/

├── app.py
├── requirements.txt
├── vercel.json
│
├── templates/
│   ├── index.html
│   └── product.html
│
├── static/
│   ├── css/
│   └── js/
│
└── README.md
```

---

# ⚙️ How It Works

```
Web Scraping
       │
       ▼
Data Cleaning
       │
       ▼
Flask REST API
       │
       ▼
JSON Response
       │
       ▼
Flask Web Application
       │
       ▼
Nintendo Deals Website
```

---

# 🎯 Learning Objectives

This project was created to practice and improve my knowledge in:

- Python development
- REST API architecture
- Web Scraping techniques
- Data transformation
- Data modeling
- Backend development
- Flask
- HTML/CSS
- JavaScript
- Responsive web design
- API consumption
- Vercel deployment
- Git & GitHub workflows

---

# 📈 Future Improvements

Some planned enhancements include:

- Product search with autocomplete
- Multiple online store integration
- Price history visualization
- Price drop alerts
- User authentication
- Favorites / Wishlist
- Product reviews
- Advanced filtering
- Dashboard with pricing analytics
- PostgreSQL database integration
- Scheduled scraping jobs
- Docker support
- CI/CD pipeline

---

# ▶️ Running Locally

Clone the repository

```bash
git clone https://github.com/yourusername/nintendo-games-web.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://localhost:5000
```

---

# 📌 Disclaimer

This project is intended for **educational and portfolio purposes**.

Product information is obtained through web scraping from publicly available sources. All trademarks, logos, and product names belong to their respective owners.

---

# 👨‍💻 About Me

I'm a **Data Analyst** passionate about healthcare analytics, Python, APIs, automation, and data engineering.

This repository is part of my continuous learning journey, where I build real-world projects to expand my software engineering and data development skills.