
# Live Music Directory

This project is a live music directory web application that allows users to register, manage their profiles, upload images and videos, list gigs, and more. The backend is built using Node.js and Express, and it stores data using CSV files rather than a traditional database.

## Features

- **User Authentication**: Register, login, and manage user sessions.
- **Profile Management**: Upload band pictures, videos, and manage profile details.
- **Gig Management**: List, view, and manage music gigs.
- **Submissions**: Users can submit their profiles for specific gigs.
- **Real-time Updates**: Receive real-time status updates using Socket.io.
- **CSV-Based Storage**: Data is stored in CSV files for simplicity and portability.

## Project Structure

### Backend

- **`data/`**: Contains the CSV files where user, gig, and submission data is stored.
  - `users.csv`: Stores user information such as username, password, and email.
  - `gigs.csv`: Stores gig information including gig name, date, location, and description.
  - `submissions.csv`: Stores submissions data linking users to gigs.
- **`routes/`**: Contains the Express route handlers for various parts of the application.
  - `auth.js`: Handles user authentication routes.
  - `profile.js`: Handles user profile-related routes.
  - `profiles.js`: Handles routes related to listing and viewing profiles.
  - `gigs.js`: Handles routes related to listing, creating, and managing gigs.
  - `submissions.js`: Handles routes related to submitting profiles for gigs.
  - `comments.js`: Handles routes related to comments on profiles or gigs.
  - `spotify.js`: Handles integration with Spotify API (if needed).
  - `likes.js`: Handles routes related to liking profiles or gigs.
- **`uploads/`**: Stores uploaded images and videos.
- **`utils/`**: Contains utility functions for handling CSV file operations.
  - `csvHandler.js`: Contains functions to read and write data to/from CSV files.
- **`.env`**: Environment variables for configuring the application (e.g., `PORT`, `RECAPTCHA_SITE_KEY`).
- **`server.js`**: The main entry point of the backend server.

### Frontend

The frontend is located in the `frontend/` directory (not detailed in this README). It is built with React and communicates with the backend API.

## Setup Instructions

### Prerequisites

- Node.js (v20.16.0 or higher)
- npm (v6 or higher)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/live-music-directory.git
   cd live-music-directory/backend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the `backend/` directory with the following content:
   ```env
   PORT=5000
   RECAPTCHA_SITE_KEY=your-recaptcha-site-key
   ```

4. Create the `data/` directory and the following CSV files within it:
   - `users.csv`:
     ```csv
     username,password,email
     ```
   - `gigs.csv`:
     ```csv
     id,name,date,location,description
     ```
   - `submissions.csv`:
     ```csv
     userId,gigId,status
     ```

5. Run the server:
   ```bash
   npm start
   ```

   The server should start on `http://localhost:5000`.

### Running the Frontend

The frontend should be built and run separately. Navigate to the `frontend/` directory and follow the React setup instructions.

### Directory Structure

```plaintext
live-music-directory/
├── backend/
│   ├── data/
│   │   ├── users.csv
│   │   ├── gigs.csv
│   │   └── submissions.csv
│   ├── routes/
│   │   ├── auth.js
│   │   ├── profile.js
│   │   ├── profiles.js
│   │   ├── gigs.js
│   │   ├── submissions.js
│   │   ├── comments.js
│   │   ├── spotify.js
│   │   └── likes.js
│   ├── utils/
│   │   └── csvHandler.js
│   ├── uploads/
│   ├── .env
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
├── frontend/
│   └── (Frontend codebase)
└── README.md
```

### Environment Variables

- `PORT`: Port number where the backend server runs.
- `RECAPTCHA_SITE_KEY`: Your Google reCAPTCHA site key.

## Usage

Once the backend and frontend are running, you can use the application to manage your band profiles, gigs, and more. The backend API endpoints can be accessed at `http://localhost:5000/api`.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request with your enhancements or fixes.

## License

This project is licensed under the MIT License.
