import React from "react";
import Sidebar from "react-sidebar";

import { Container, Col, Row, ListGroup } from "react-bootstrap";

export default function CVSidebar(props) {
  return (
    <Sidebar
      sidebar={
        <ListGroup as="ul">
          <ListGroup.Item as="li" active>
            Poland
          </ListGroup.Item>
          <ListGroup.Item as="li">Germany</ListGroup.Item>
          <ListGroup.Item as="li" disabled>
            USA
          </ListGroup.Item>
          <ListGroup.Item as="li">UK</ListGroup.Item>
        </ListGroup>
      }
      docked={true}
      styles={{ root: { top: 52}, sidebar: {width: 100} }}
    >
      {props.children}
    </Sidebar>
  );
}
