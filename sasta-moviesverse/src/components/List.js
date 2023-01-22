import React from "react";
// import { fetchData } from "../api/api";

const List = (props) => {
  return (
    <div className="list">
      <div className="row">
        <h2 className="text-white title">{props.title}</h2>
        <div className="col">
          <div className="row__posters">
            {props.data.map((item) => (
              // <img
              //   className="row__poster row__posterLarge"
              //   src={""}
              //   alt={item}
              // />
              <p className="info">{item} ,</p>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default List;
