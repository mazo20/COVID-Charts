import React, { PureComponent } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  Legend
} from "recharts";

const data = [
  {
    name: "03.08",
    Poland: 11,
    CzechRepublic: 31,
    Germany: 5
  },
  {
    name: "03.09",
    Poland: 16,
    CzechRepublic: 31,
    amt: 2400
  },
  {
    name: "03.10",
    Poland: 22,
    CzechRepublic: 41,
    amt: 2400
  },
  {
    name: "03.11",
    Poland: 31,
    CzechRepublic: 91,
    amt: 2400
  },
  {
    name: "03.12",
    Poland: 49,
    CzechRepublic: 94,
    amt: 2400
  },
  {
    name: "03.13",
    Poland: 68,
    CzechRepublic: 141,
    amt: 2210
  },
  {
    name: "03.14",
    Poland: 103,
    CzechRepublic: 189,
    amt: 2290
  },
  {
    name: "03.15",
    Poland: 119,
    CzechRepublic: 253,
    amt: 2000
  },
  {
    name: "03.16",
    Poland: 177,
    CzechRepublic: 298,
    amt: 2181
  },
  {
    name: "03.17",
    Poland: 238,
    CzechRepublic: 396,
    amt: 2500
  },
  {
    name: "03.18",
    Poland: 251,
    CzechRepublic: 464,
    amt: 2100
  }
];

export default class Example extends PureComponent {
  static jsfiddleUrl = "https://jsfiddle.net/alidingling/xqjtetw0/";

  render() {
    return (
      <ResponsiveContainer width="100%" aspect={5.0 / 3.0}>
        <LineChart
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            isAnimationActive={false}
            type="monotone"
            dataKey="CzechRepublic"
            stroke="#8884d8"
            activeDot={{ r: 3 }}
            strokeWidth={2}
          />
          <Line
            isAnimationActive={false}
            type="monotone"
            dataKey="Poland"
            stroke="#82ca9d"
            strokeWidth={2}
            activeDot={{ r: 3 }}
          />
        </LineChart>
      </ResponsiveContainer>
    );
  }
}
