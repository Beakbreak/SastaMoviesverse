import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Linked from "./linked";

const List = (props) => {
  return (
    <div className="list">
      <div className="row">
        <h2 className="text-white title">{props.title}</h2>
        <div className="col">
          <div className="row__posters">
            {/* <Router>
              <Routes> */}
            {props.data.map((item) => (
              // <img
              //   className="row__poster row__posterLarge"
              //   src={""}
              //   alt={item}
              // />
              // <Route
              //   exact
              //   path="/linked"
              //   element={<Linked moviedata={item} />}
              // />
              <p className="info">{item},</p>
            ))}
            {/* </Routes>
            </Router> */}
          </div>
        </div>
      </div>
    </div>
  );
};

export default List;
