import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import reportWebVitals from './reportWebVitals';

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import {
  Navigation,
  Footer,
  Home,
  SimpleAI,
  MCTSAI, 
  NoUcbMCTSAI,
  OpenLoopMCTSAI
} from "./components";


ReactDOM.render(
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/simpleAI" element={<SimpleAI />} />
      <Route path="/mctsAI" element={<MCTSAI />} />
      <Route path="/noUcbMCTSAI" element={<NoUcbMCTSAI />} />
      <Route path="/openLoopMCTSAI" element={<OpenLoopMCTSAI />} />

    </Routes>
    <Footer />

    <div class="container">
        <div class="row align-items-center my-5">
          <div class="col-lg-0">
          </div>
          <div class="col-lg-0">

          <strong><span style={{color: "#4c7ddd"}}>Author: </span></strong>
          <span> Carlos García-Lemus </span>
          <br />
          <strong><span style={{color: "#4c7ddd"}}>Advisor: </span></strong>
          <span> Dr. Canaan </span>
          <br />
          <strong><span style={{color: "#4c7ddd"}}>Course: </span></strong>
          <span> CSC 491 Senior Project II </span>
          <br />
          <strong><span style={{color: "#4c7ddd"}}>Affiliation: </span></strong>
          <span> California Polytechnic University, San Luis Obispo
              Computer Science Department </span>
          <br />
          <strong><span style={{color: "#4c7ddd"}}>Completion Date: </span></strong>
          <span> TBD </span>
          </div>
        </div>
      </div>
    
  </Router>,

  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
