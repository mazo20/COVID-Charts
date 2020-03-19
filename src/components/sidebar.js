import React from "react";
import Sidebar from "react-sidebar";

import { ListGroup } from "react-bootstrap";

import { useCountryState } from '../context/country';


export default function CVSidebar(props) {
  const countryContext = useCountryState();

  return (
    <Sidebar
      sidebar={
        <ListGroup as="ul">
          {
            countryContext.countries.map((country) => {
              return (
                <ListGroup.Item as="li"
                  active={country == countryContext.country}
                  action onClick={() => { countryContext.setCountry(country); }}>
                  {country}
                </ListGroup.Item>
              );
            })
          }
        </ListGroup>
      }
      docked={true}
      styles={{ root: { top: 52 }, sidebar: { width: 100 } }}
    >
      {props.children}
    </Sidebar>
  );
}
