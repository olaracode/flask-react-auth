import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const initialValue = {
  email: "",
  password: "",
};

export const Home = () => {
  const { store, actions } = useContext(Context);
  const [registerData, setRegisterData] = useState(initialValue);

  const handleChange = (event) => {
    // Va a modificar nuestro estado cuando usemos los inputs
    setRegisterData({
      ...registerData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = () => {
    actions.registerUser(registerData);
  };

  return (
    <div className="text-center mt-5">
      <div className="container">Registrate</div>
      <div className="card p-5">
        <input
          placeholder="email"
          type="email"
          name="email"
          onChange={handleChange}
        />
        <input
          placeholder="password"
          type="password"
          name="password"
          onChange={handleChange}
        />
        <button onClick={handleSubmit}>Registrar usuario</button>
      </div>
    </div>
  );
};
