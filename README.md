# BrightFuturesHub

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
BrightFuturesHub is a web platform dedicated to empowering First-Generation and Low-Income (FGLI) students by providing a comprehensive suite of tools and resources. The platform aims to bridge the gap between opportunities and support for FGLI students, helping them succeed academically, professionally, and personally.

## Features
- **Work-Study Matchmaking:** Connects FGLI students with relevant part-time job opportunities, internships, and work-study positions that align with their academic schedules and career aspirations.
- **Community Building Events:** Organizes a variety of workshops, seminars, and networking events specifically tailored to FGLI students. These events focus on skill development, career guidance, mental health support, and fostering a sense of community.
- **Emergency Aid Crowdfunding:** Provides a crowdfunding platform where FGLI students can raise funds during unexpected financial emergencies such as medical bills, housing issues, or unforeseen car repairs.

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** Sqlite

## Getting Started
1. Fork the repository

2. Clone the repository: 
`git clone https://github.com/yourusername/BrightFuturesHub.git
cd BrightFuturesHub`

3. Create a virtual environment:
`python3 -m venv venv`
`source venv/bin/activate (Linux/Mac)`
`venv\Scripts\activate (Windows)`

4. Install dependencies:
`pip install -r requirements.txt`

5. Set up the database:
`python manage.py makemigrations`
`python manage.py migrate`

6. Run the development server:
`python manage.py runserver`

## Usage
Visit `http://localhost:8000` in your web browser to access the BrightFuturesHub application. Explore the different features, including work-study matchmaking, community events, and accessing resources tailored to FGLI students' needs.

## Contributing
We welcome contributions to improve BrightFuturesHub! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).