import React, { useState, useEffect } from "react";
import {
  useTheme,
  Box,
  Button,
  Card,
  styled,
} from "@mui/material";
import ReactEcharts from "echarts-for-react";
import axios from "axios";

const CardHeader = styled(Box)(() => ({
  display: "flex",
  paddingLeft: "24px",
  paddingRight: "24px",
  marginBottom: "12px",
  alignItems: "center",
  justifyContent: "space-between",
}));

const Title = styled("span")(() => ({
  fontSize: "1rem",
  fontWeight: "500",
  textTransform: "capitalize",
}));

const StyledButton = styled(Button)(({ theme }) => ({
  margin: theme.spacing(1),
}));

const LatestActivity = () => {
  const theme = useTheme();
  
  const [data, setData] = useState([]);
  const [timeRange, setTimeRange] = useState("5m");
  
  const fetchData = async () => {
    try {
      const response = await axios.get(`/api/timelast/${timeRange}`);
      const formattedData = formatData(response.data);
      setData(formattedData);
    } catch (error) {
      console.error(`Failed to load /api/timelast/${timeRange}`, error);
    }
  };
  
  const formatData = (data) => {
    let formattedData = {
      timestamp: [],
      class0: [],
      class1: [],
      class2: [],
    };
    
    let groupedData = {};
    
    data.forEach(item => { 
      if(!groupedData[item.timestamp]) {
        groupedData[item.timestamp] = {class0: 0, class1: 0, class2:0 };
      }
      groupedData[item.timestamp][`class${item.class}`] = item.probability;
    });
    
    let sortedTimestamps = Object.keys(groupedData).sort((a, b) => new Date(a) - new Date(b));
    
    sortedTimestamps.forEach(timestamp => {
      formattedData.timestamp.push(timestamp);
      formattedData.class0.push(groupedData[timestamp].class0);
      formattedData.class1.push(groupedData[timestamp].class1);
      formattedData.class2.push(groupedData[timestamp].class2);
    });     
    
    return formattedData;
  }
  
  useEffect(() => {
    fetchData();
  }, [timeRange]);
  
  const options = {
    legend: {
      show: true,
      itemGap: 20,
      icon: "circle",
      bottom: 10,
      textStyle: {
        color: theme.palette.text.secondary,
        fontSize: 13,
        fontFamily: "roboto",
      },
    },
    tooltip: {
      show: false,
      trigger: "axis",
      formatter: "{a} <br/>{b}: {c}",
    },
    xAxis: [
      {
        type: "category",
        data: data.timestamp,
        axisLine: {
          show: true,
        },
        splitLine: {
          show: true,
        },
      },
    ],
    yAxis: [
      {
        type: "value",
        axisLine: {
          show: true,
        },
        splitLine: {
          show: false,
        },
      },
    ],
    series: [
      {
        name: "Fly",
        type: "line",
        stack: "total",
        areaStyle: {},
        data: data.class2,
      },
      {
        name: "Cricket",
        type: "line",
        stack: "total",
        areaStyle: {},
        data: data.class1,
      },
      {
        name: "Control",
        type: "line",
        stack: "total",
        areaStyle: {},
        data: data.class0,
      },
    ],
  };
  
  return (
    <Card elevation={3} sx={{ pt: "20px", mb: 3 }}>
    <CardHeader>
    <Title>Insect Activity</Title>
    </CardHeader>
    
    <Box sx={{ 
      display: "flex", 
      justifyContent: "center", 
      alignItems: "center",
      mb: 2
    }}>
    <StyledButton variant="outlined" color="inherit" onClick={() => setTimeRange("5m")}>5 minutes</StyledButton>
    <StyledButton variant="outlined" color="inherit" onClick={() => setTimeRange("15m")}>15 minutes</StyledButton>
    <StyledButton variant="outlined" color="inherit" onClick={() => setTimeRange("1h")}>1 hour</StyledButton>
    <StyledButton variant="contained" color="primary" onClick={fetchData}>Refresh Data</StyledButton>
    </Box>
    <Box sx={{ 
      justifyContent: "center", 
      alignItems: "center",
      mb: 2
    }}>
    <ReactEcharts option={options} />
    </Box>
    </Card>
    );
  }
  
  export default LatestActivity;