# Interactive Dashboard with Next.js and Django

This project is an interactive dashboard application built with Next.js for the frontend and Django for the backend API. It features a responsive design with various charts displaying data fetched from the backend.

## Setup Instructions

### Prerequisites
- Node.js (v14 or later)
- Python (v3.8 or later)
- Docker (optional, for containerized setup)

### Frontend Setup (Next.js)

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`.

### Backend Setup (Django)

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the Django server:
   ```
   python manage.py runserver
   ```

The backend API will be available at `http://localhost:8000`.

### Docker Setup (Optional)

To run both frontend and backend in Docker containers:

1. Build the Docker images:
   ```
   docker-compose build
   ```

2. Start the containers:
   ```
   docker-compose up
   ```

The frontend will be available at `http://localhost:3000` and the backend at `http://localhost:8000`.

## Libraries and Tools Used

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion
- Lucide React (for icons)
- Axios (for API requests)
- ApexCharts (for data visualization)

### Backend
- Django
- Django REST Framework
- Django CORS Headers

### Development Tools
- ESLint
- Prettier
- Docker & Docker Compose

## Approach and Thought Process

1. **TypeScript Integration**: We used TypeScript for type safety and better developer experience in the Next.js app.

2. **Component Structure**: The dashboard is built with reusable components (e.g., KPICard, ChartContainer) for maintainability and scalability.

3. **Responsive Design**: Tailwind CSS is used for a responsive layout that adapts to different screen sizes.

4. **Data Fetching**: We implement data fetching in the frontend using Axios, with the option to use Next.js API routes for additional server-side processing if needed.

5. **Animations**: Framer Motion is used for smooth animations and transitions, enhancing the user experience.

6. **Backend API**: Django REST Framework is used to create a robust API, serving mock data for the charts and KPIs.

7. **CORS Handling**: Django CORS Headers is implemented to handle Cross-Origin Resource Sharing, allowing the frontend to communicate with the backend.

8. **Docker Integration**: Docker and Docker Compose are used for easy setup and consistent development environments.

## Bonus Features Implemented

1. **TypeScript**: The entire Next.js application is written in TypeScript for improved type safety and developer experience.

2. **Docker**: Docker and Docker Compose files are provided for containerized setup of both frontend and backend.

3. **State Management**: While not fully implemented, the project is structured to easily integrate a state management solution like Redux or React Context API if needed in the future.

## Future Improvements

- Implement full state management solution (e.g., Redux) for more complex data handling.
- Add more comprehensive test coverage, including integration tests.
- Implement user authentication and authorization.
- Optimize performance with server-side rendering or static generation for suitable pages.