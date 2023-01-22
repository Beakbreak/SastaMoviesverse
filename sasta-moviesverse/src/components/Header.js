import { useNavigate, Link } from "react-router-dom";

import react, { useState } from 'react';

const Header = () => {
  const navigate = useNavigate();
  const [isLoggedin, setisLoggedin] = useState(false);

  const clickHandler = (e) => {
    e.preventDefault();
    navigate('/login');
  }
  const clickHandler2 = (e) => {
    e.preventDefault();
    navigate('/register');
  }
  const clickHandler3 = (e) => {
    e.preventDefault();
    localStorage.removeItem('token-info');
    setisLoggedin(false);
    navigate('/');
  }
  if (localStorage.getItem('token-info')) {
    setisLoggedin(true);
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
              {!isLoggedin && <button className="btn btn-info signup" onClick={clickHandler2}>SignUp</button>}
              {!isLoggedin && <button className="btn btn-danger" onClick={clickHandler}>SignIn</button>}
              {isLoggedin && <button className="btn btn-danger" onClick={clickHandler3}>Logout</button>}
            </form>
          </div>
        </div>
      </nav>
    </header>
  )
}

export default Header;