import React, { Component } from "react";
import "./App.css";
import Game from "./Game/Game";

class App extends Component {
  render() {
    console.log(process.env.PUBLIC_URL)
    return (
      <div className="App">
        <header className="App-header" />
        <Game publicUrl={process.env.PUBLIC_URL} />
      </div>
    );
  }
}

export default App;
