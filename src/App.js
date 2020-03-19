import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Example from "./charts/testChart";

import { Container, Col, Row } from "react-bootstrap";
import Sidebar from "react-sidebar";

import CVNavbar from "./components/navbar";

function App() {
  return (
    <div className="App">
      <CVNavbar></CVNavbar>
      <div
        style={{
          margin: 200
        }}
      ></div>
      <Sidebar sidebar={<b>Wojtek debil</b>} docked={true} styles={{ root: { top: 52 } }}>
        <h1
          style={{
            margin: 20
          }}
        >
          Poland
        </h1>
        <Container
          fluid="sm"
          style={{
            marginTop: 100
          }}
        >
          <Col>
            <Example></Example>
            <Example></Example>
            <Example></Example>
          </Col>
        </Container>
      </Sidebar>
    </div>
  );
}

export default App;
