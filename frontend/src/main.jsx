import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router";
import App from "./App.jsx";
import './style.css'

const root = document.getElementById("root");

ReactDOM.createRoot(root).render(
  <BrowserRouter >
    {/* <Routes>
  <Route path="/ap" element={<App />}>
    <Route index element={<Signup />} />
  </Route>
</Routes> */}
<App />
  </BrowserRouter>,
);
