import React from "react";

const Linked = (props) => {
  return (
    <>
      <h1>{props.moviedata}</h1>
      <select>
        Choose rating
        <option value={0}>0</option>
        <option value={1}>1</option>
        <option value={2}>2</option>
        <option value={3}>3</option>
        <option value={4}>4</option>
        <option value={5}>5</option>
      </select>
    </>
  );
};

export default Linked;
