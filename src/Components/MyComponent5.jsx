import React, { useEffect, useState } from 'react';
import {
    LineChart,
    Line,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend
} from "recharts";
import $ from 'jquery';

const MyComponent5 = () => {
    const [responseData, setResponseData] = useState(null);
    const [finalboss, setFinalBoss] = useState([]);

    useEffect(() => {
        const fetchData = () => {
            $.ajax({
                url: 'https://api.thingspeak.com/channels/2413959/feeds.json?api_key=E6J3X5VUYCB6LH9D&results=10',
                method: 'GET',
                dataType: 'json',
                success: function (response) {
                    setResponseData(response);
                },
                error: function (xhr, status, error) {
                    console.error('Error fetching data:', error);
                }
            });
        };
        fetchData();
        const interval = setInterval(fetchData, 5000);
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        if (responseData) {
            const newFinalBoss = responseData.feeds
                .filter(element => element.field5 !== null)
                .map(element => {
                    const timeval = element.created_at.slice(11, 19);
                    const timeFormatted = timeval.slice(0, 2) + timeval.slice(3, 5);
    
                    return {
                        "val": element.field5,
                        "Time": timeFormatted
                    };
                });
            setFinalBoss(newFinalBoss);
        }
    }, [responseData]);

    return (
        <>
            <LineChart
                width={500}
                height={300}
                data={finalboss}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line
                    type="monotone"
                    dataKey="val"
                    stroke="#ff0000"
                    activeDot={{ r: 8 }}
                />
            </LineChart>
        </>
    );
};

export default MyComponent5;
