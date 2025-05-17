CSV Extractor API Project Setup Guide

Here's a detailed, point-by-point guide for running the CSV Extractor API project:

1. Clone the repository
   - Use `git clone [repository-url]` to clone the project to your local machine
   - Navigate to the project directory with `cd src`

2. Set up a virtual environment
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`

3. Install dependencies
   - Install all required packages: `pip install -r requirements.txt`

4. Apply database migrations
   - Generate migration files: `python manage.py makemigrations`
   - Apply migrations to the database: `python manage.py migrate`

## Running the Application

5. Start the development server
   - Launch the server: `python manage.py runserver`
   - The server will start at: http://127.0.0.1:8000/

6. Access the API endpoint
   - The CSV upload endpoint is available at: http://127.0.0.1:8000/api/csv-upload/
   - Use POST requests to interact with this endpoint

## Using the API

7. Send CSV data
   - Make POST requests with a CSV file attached
   - The CSV must contain columns for:
     - name (required, non-empty string)
     - email (required, valid email format)
     - age (required, integer between 0-120)

8. **Testing tools**
   - Use Postman to send requests with CSV files attached
   - Alternative: Use curl command in terminal
   - Example curl command:
     ```
     curl -X POST -F "file=@your_file.csv" http://127.0.0.1:8000/api/csv-upload/
     ```

## Testing

9. Run unit tests
   - Execute all tests: `python manage.py test`
   - Tests verify:
     - Successful record creation with valid data
     - Proper error handling for invalid inputs
     - Edge case handling

10. Test case coverage
    - Valid CSV file processing and database storage
    - Invalid email format detection and rejection
    - Empty name field validation
    - Age constraints (must be 0-120)
    - File format validation (must be .csv)
    - Empty file handling
    - Malformed CSV structure detection

11. View test results
    - The test runner will display passed/failed tests
    - Debug information is provided for any failures

12. Troubleshooting
    - Ensure database connection settings are correct
    - Verify all dependencies are properly installed
    - Check file permissions if upload functionality fails
