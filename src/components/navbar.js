import React from "react";

import {
  Navbar,
  Nav,
} from "react-bootstrap";

export default function CVNavbar() {
  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand href="#home">COVID-19 Charts</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#link">Data source</Nav.Link>
        </Nav>
        <Nav inline>
          <Nav.Link href="#home">About</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}
