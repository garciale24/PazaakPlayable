import React from "react";
import { NavLink } from "react-router-dom";

function Navigation() {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">

          <NavLink className="navbar-brand" to="/">
            MCTS Pazaak
          </NavLink>
          <div>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Home
                  <span className="sr-only">(current)</span>
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/simpleAI">
                  SimpleAI
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/mctsAI">
                  MCTSAI
                </NavLink>
              </li>

              
              <li className="nav-item">
                <NavLink className="nav-link" to="/noUcbMCTSAI">
                  NoUCBMCTSAI
                </NavLink>
              </li>

              <li className="nav-item">
                <NavLink className="nav-link" to="/openLoopMCTSAI">
                  OpenLoopMCTSAI
                </NavLink>
              </li>

            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navigation;