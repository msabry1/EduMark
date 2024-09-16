# EduMark

EduMark is a Django-based educational platform that offers course management and browsing functionality.

## Features

- Course Management: Add, view, and manage courses
- Category System: Organize courses into categories
- Search Functionality: Search courses by name, description, or required skills
- Pagination: Implemented for course listings
- Course Statistics: Calculate total hours, video numbers, and tutorials across all courses
- User Authentication: Login and logout functionality
- Responsive Design: Courses displayed with pagination (6 per page)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/msabry1/EduMark.git
   cd EduMark
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Django project settings, including database configuration and secret key.

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to the homepage to view featured courses and categories.
2. Use the search functionality to find specific courses.
3. Browse courses by category.
4. View detailed information about each course.
5. Access the about page to see overall platform statistics.

## Project Structure

- `about`: Calculates and displays overall course statistics
- `contact`: Renders the contact page
- `courses`: Handles course listing, searching, and pagination
- `course`: Displays individual course details
- `homepage`: Renders the main page with featured courses and categories
- `logout`: Handles user logout functionality
