import { useNavigate, Link } from "react-router-dom";

import react, { useState } from "react";

const Header = (props) => {
  const navigate = useNavigate();
  const check = props.l;
  const [x, setx] = useState(check);
  const clickHandler = (e) => {
    e.preventDefault();
    navigate("/login");
  };
  const clickHandler2 = (e) => {
    e.preventDefault();
    navigate("/register");
  };
  const clickHandler3 = (e) => {
    e.preventDefault();
    localStorage.removeItem("token-info");
    setx(false);
    navigate("/");
  };

  return (
    <header className="topNav">
      <nav className="navbar navbar-expand-md navbar-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <b className="nav__logo logo">MOVIESVERSE</b>
          </Link>

          <div className="navbar">
            <form className="d-flex" role="search">
              {!x && (
                <button className="btn btn-info signup" onClick={clickHandler2}>
                  SignUp
                </button>
              )}
              {!x && (
                <button className="btn btn-danger" onClick={clickHandler}>
                  SignIn
                </button>
              )}
              {x && (
                <button className="btn btn-danger" onClick={clickHandler3}>
                  Logout
                </button>
              )}
            </form>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
