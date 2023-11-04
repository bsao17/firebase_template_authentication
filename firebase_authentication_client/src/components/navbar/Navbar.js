// Navbar.js
import React from 'react';
import './Navbar.css';

// Ce composant fonctionnel Navbar rendra la barre de navigation
const Navbar = () => {
  return (
    <header className="navbar">
      
      <div className="navbar__title navbar__item">MaApp</div>
      <div className="navbar__item">
        <a href="/" className="navbar__link">Accueil</a>
      </div>
      <div className="navbar__item">
        <a href="https://localhost:5000/login" className="navbar__link">Services</a>
      </div>
      <div className="navbar__item">
        <a href="/contact" className="navbar__link">Contact</a>
      </div>
     
    </header>
  );
};

export default Navbar;
