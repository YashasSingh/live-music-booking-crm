import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    axios.get('/api/bookings')
      .then(response => {
        setBookings(response.data.bookings);
      })
      .catch(error => {
        console.error('Error fetching bookings:', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Live Music Bookings</h1>
      <ul>
        {bookings.map((booking, index) => (
          <li key={index}>{booking}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
