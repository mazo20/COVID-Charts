import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Example from "./charts/testChart";

import { Container, Col, Row, ListGroup } from "react-bootstrap";

import CVNavbar from "./components/navbar";
import Sidebar from "./components/sidebar";

import { useCountryState } from './context/country';

function App() {
    const countryContext = useCountryState();

    return (
        <div className="App">
            <CVNavbar></CVNavbar>
            <div style={{ margin: 200 }}></div>
            <Sidebar>
                <h1 style={{ margin: 20 }}>
                    {countryContext.country}
                </h1>
                <Container style={{ marginTop: 100 }}>
                    <Row>
                        <Col>
                            <Example></Example>
                        </Col>
                        <Col>
                            <Example></Example>
                        </Col>
                        <Col>
                            <Example></Example>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Example></Example>
                        </Col>
                        <Col>
                            <Example></Example>
                        </Col>
                        <Col>
                            <Example></Example>
                        </Col>
                    </Row>
                </Container>
            </Sidebar>
        </div>
    );
}

export default App;
