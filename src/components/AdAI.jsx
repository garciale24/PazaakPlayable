import React from "react";

function AdAI() {
  return (
    <div className="AdAI">

      <div class="container">
        <div class="row align-items-center my-4">
          <div class="col-lg-0">

          </div>
          <div class="col-lg-0">
            <h1 class="font-weight-heavy">AI Games Played</h1>

            <span> NOTE: 'Open Loop MCTS AI' is actually 'No Expansion MCTS AI' for the following visuals: </span>

          </div>
        </div>
      </div>

    <iframe scrolling="no" title="Tab1" width="1200" height="1000px" src="https://public.tableau.com/views/Book2_16466462420050/Sheet1?:embed=y&:display_count=yes&:showVizHome=no">
    </iframe>
    <br></br>
    <iframe scrolling="no" title="Tab2" width="1200" height="500px" src="https://public.tableau.com/views/Book2_1_16466464238500/Sheet2?:embed=y&:display_count=yes&:showVizHome=no">
    </iframe>
    </div>
  );
}

export default AdAI;