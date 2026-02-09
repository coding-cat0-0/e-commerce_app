import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Signup from "./components/register";
import Login from "./components/login";
import Home from "./components/Home";


function App() {
  return (

    <>
<Routes>
  {/* <Route path="/" element={<Home />} /> */}
  <Route path="/signup" element={<Signup />} />
  <Route path="/login" element={<Login />} />
</Routes>
</>

  );
}

export default App;