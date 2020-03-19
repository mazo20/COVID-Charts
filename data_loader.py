#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:05:58 2020

@author: wojtekadamczyk
"""

import pandas as pd



def produce_json_from_url(url):
    df = (pd.read_csv(url))
    df = df.set_index('Country/Region').transpose().drop(['Province/State', 'Lat', 'Long']).reset_index()
    df = df.groupby(df.columns, axis=1).sum() #Sum over all US states, and provinces of other countries
    df = df.rename(columns={'index': 'name'})
    json = df.to_json(orient='records')
    return json

url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

json_deaths = produce_json_from_url(url_deaths)
json_confirmed = produce_json_from_url(url_confirmed)
json_recovered = produce_json_from_url(url_recovered)
