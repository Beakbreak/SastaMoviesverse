import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import linked from "linked";
const List = (props) => {
  return (
    <div className="list">
      <div className="row">
        <h2 className="text-white title">{props.title}</h2>
        <div className="col">
          <div className="row__posters">
            <BrowserRouter>
              <Routes>
                {props.data.map((item) => (
                  // <img
                  //   className="row__poster row__posterLarge"
                  //   src={""}
                  //   alt={item}
                  // />

                  <Route path="linked" element={<linked moviedata={item} />}></Route>
                ))}
              </Routes>
            </BrowserRouter>
          </div>
        </div>
      </div>
    </div>
  );
};

export default List;
