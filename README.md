# My Illini

## Overview
My Illini is a course management system developed as a final project for CS 411 at the University of Illinois at Urbana-Champaign (UIUC). The application provides a platform for managing course information, viewing course statistics, and facilitating course-related discussions.

## Features

### Course Management
- View comprehensive course listings
- Add new courses with detailed information:
  - Year/Term
  - Subject
  - CRN (Course Reference Number)
  - Course Code
  - Course Title
  - Instructor
  - Average GPA
- Edit existing course information
- Delete courses

### Search and Analytics
- Search courses by CRN
- View top 15 courses by GPA
- Browse complete course catalog

### Discussion System
- Post comments about courses
- View all course-related discussions
- Manage and moderate comments

## Technology Stack
- **Backend**: Python Flask
- **Database**: Google Cloud Platform (GCP)
- **Frontend**: HTML/CSS templates
- **Dependencies**:
  - Flask
  - Flask-SQLAlchemy
  - PyMySQL
  - PyYAML

## Project Structure

CS 411 Final Project @UIUC

Data hosted on GCP. Website was built with flask.

## Setup Instructions

### Prerequisites
- Python 3.x
- GCP account with necessary credentials
- MySQL database (hosted on GCP)

### Installation Steps
1. Clone the repository
```bash
git clone [your-repository-url]
cd my-illini
```

2. Set up Python virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages
```bash
pip install flask flask-sqlalchemy pymysql pyyaml
```

4. Configure GCP credentials
- Ensure your GCP credentials are properly set up
- Configure database connection settings

5. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome page |
| `/courses` | GET/POST | View/add courses |
| `/courses/edit/<code>` | GET/POST | Edit course information |
| `/courses/delete/<code>` | POST | Delete a course |
| `/post` | GET/POST | View/add comments |
| `/post/delete/<id>` | POST | Delete comments |
| `/search` | GET/POST | Search courses by CRN |
| `/searchTop15` | GET | View top 15 courses by GPA |

## Database

The application uses a MySQL database hosted on Google Cloud Platform (GCP) to store:
- Course information
- User comments
- Course statistics

## Contributing
This project was developed as part of CS 411 at UIUC. For any improvements or bug fixes, please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Team
- Grace Chang

## Acknowledgments
- CS 411 Course Staff at UIUC
- Google Cloud Platform for hosting services

## License
This project is part of academic coursework at UIUC.
