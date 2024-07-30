document.getElementById('eventForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Gather form data
    const artist = document.getElementById('artist').value;
    const venue = document.getElementById('venue').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const stage = document.getElementById('stage').value;

    // Here you would typically send data to the backend
    console.log(`Booking Event: ${artist} at ${venue} on ${date} at ${time} on stage ${stage}`);
    
    // Clear the form
    event.target.reset();
});
