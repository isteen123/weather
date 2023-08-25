import React, { useState } from 'react';
import axios from 'axios';
import './WeatherApp.css'

function WeatherApp() {
  const [location, setLocation] = useState('');
  const [weatherData, setWeatherData] = useState(null);

  const fetchWeather = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/weather?location=${location}`);
      setWeatherData(response.data);
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  return (
    <div>
      <h1>Weather App</h1>
      <input
        type="text"
        placeholder="Enter location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>
      {weatherData && (
        <div className="weather-card">
          <img
        className="weather-icon"
        src="/weather1.jpg" // Update the image path
        alt="Weather Icon"
      />
        <h2>{weatherData.location}</h2>
        <p>Temperature: {weatherData.temperature}°C</p>
        <p>Humidity: {weatherData.humidity}%</p>
        <p>Conditions: {weatherData.conditions}</p>
      </div>
      )}
    </div>
  );
}

export default WeatherApp;
