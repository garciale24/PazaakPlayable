import React from "react";

function HowToPlay() {
  return (
    <div className="howToPlay">
      <div class="container">
      <div class="row align-items-center my-2">
          <div class="col-lg-4">

          </div>
          <div class="col-lg-5">
            {/*<h1 class="font-weight-light">How To Play</h1>*/}
            
          </div>
          </div>      
          <iframe title="how to play pazaak" src="https://docs.google.com/document/d/e/2PACX-1vRKV3acIaeO-nrlKP8sONu5RXFPfCkkDiY8EwVf05YhFMGuvNEvj44EOJ5OWRoSJdzEDWtR2ox4MfPc/pub?embedded=true" height="1850" width= "850" scrolling="no"seamless="seamless" frameborder="0" 
      ></iframe>
      <iframe width="650" height="415" src="https://www.youtube.com/embed/9m3dxk8wWSo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      <br></br><br></br>
      </div>
    </div>
  );
}

export default HowToPlay;