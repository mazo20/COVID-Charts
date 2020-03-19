import React, { createContext, useContext, useState, useEffect } from 'react';

const CountryContext = createContext();

export const CountryProvider = props => {
    const countries = ["Poland", "Germany", "USA", "UK"];
    const [country, setCountry] = useState('Poland');

    //Expose the state and functions in provider
    const getValues = () => {
        return {
            countries: countries,
            country: country,
            setCountry: setCountry
        };
    };

    return (
        <CountryContext.Provider value={getValues()}>
            {props.children}
        </CountryContext.Provider>
    );
};

export function useCountryState() {
    const context = useContext(CountryContext);
    if (context === undefined) {
        throw new Error(
            'useCountryState must be used within a CountryProvider',
        );
    }
    return context;
}
