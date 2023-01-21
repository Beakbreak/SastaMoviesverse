import { useNavigate, Link } from "react-router-dom";
import React from 'react';

const Header = () => {
  const navigate = useNavigate();

  const clickHandler = (e) => {
    e.preventDefault();
    navigate('/login');
  }
  const clickHandler2 = (e) => {
    e.preventDefault();
    navigate('/register');
  }

  return (
    <header className="topNav">
      <nav className="navbar navbar-expand-md navbar-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <b className="nav__logo logo">MOVIESVERSE</b>
          </Link>

          <div className="navbar">
            <form className="d-flex" role="search">
              <button className="btn btn-info signup" onClick={clickHandler2}>SignUp</button>
              <button className="btn btn-danger" onClick={clickHandler}>SignIn</button>
            </form>
          </div>
        </div>
      </nav>
    </header>
  )
}

export default Header;