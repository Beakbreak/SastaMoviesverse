import React from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Linked from "./linked";
import Modal from 'react-modal'

Modal.setAppElement("#root");


const List = (props) => {
  const [modalIsOpen, setIsOpen] = useState(false);

  const openModal = () => {
    setIsOpen(true);
  };

  const closeModal = () => {
    setIsOpen(false);
  };
  const lol = (form) => {
    const formData = new FormData();
    const plainFormData = Object.fromEntries(formData.entries())

    fetch("http://localhost:8000/rating", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        email: email,
        rating: plainFormData.rating,
        movie_id: 460,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
  }
  return (
    <div className="list">
      <div className="row">
        <h2 className="text-white title">{props.title}</h2>
        <div className="col">
          <div className="row__posters">


            {props.data.map((item) => (

              <>
                <p onClick={openModal}>{item}</p>
                <Modal
                  isOpen={modalIsOpen}
                  onRequestClose={closeModal}
                  style={modalStyles}
                  moviedata={item}
                >
                  <h2>{moviedata}</h2>
                  <h3>Rate this movie:</h3>
                  <form onSubmit={() => lol(this)}>
                    <input type="number" id="rating" />
                    <button onClick={closeModal}>close</button>
                    <button type="submit">Submit</button>
                  </form>
                </Modal></>

            ))}

          </div>

        </div>
      </div>
    </div>
  );
};

export default List;
