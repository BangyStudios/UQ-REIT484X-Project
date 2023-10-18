import React from 'react';
import { useTheme } from '@mui/material';
import ReactEcharts from 'echarts-for-react';
import axios from "axios";
import { useState, useEffect } from "react";

const DoughnutChart = ({ height, color = [] }) => {
  const theme = useTheme();
  const [classProbabilities, setClassProbabilities] = useState([]);

  useEffect(() => {
    axios.get("/api/count/probability")
      .then(response => {
        setClassProbabilities(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const getClassName = (classId) => {
    switch (classId) {
      case "0":
        return "Control (None)";
      case "1":
        return "Cricket";
      case "2":
        return "Fly";
      default:
        return `Class ${classId}`;
    }
  };

  const processedData = classProbabilities.map(entry => ({
    value: entry.totalProbability,
    name: getClassName(entry.classId)
  }));

  const option = {
    legend: {
      show: true,
      itemGap: 20,
      icon: 'circle',
      bottom: 0,
      textStyle: {
        color: theme.palette.text.secondary,
        fontSize: 13,
        fontFamily: 'roboto'
      }
    },
    tooltip: {
      show: false,
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    xAxis: [
      {
        axisLine: {
          show: false
        },
        splitLine: {
          show: false
        }
      }
    ],
    yAxis: [
      {
        axisLine: {
          show: false
        },
        splitLine: {
          show: false
        }
      }
    ],

    series: [
      {
        name: 'Insect Activity',
        type: 'pie',
        radius: ['45%', '72.55%'],
        center: ['50%', '50%'],
        avoidLabelOverlap: false,
        hoverOffset: 5,
        stillShowZeroSum: false,
        label: {
          normal: {
            show: false,
            position: 'center', // shows the description data to center, turn off to show in right side
            textStyle: {
              color: theme.palette.text.secondary,
              fontSize: 13,
              fontFamily: 'roboto'
            },
            formatter: '{a}'
          },
          emphasis: {
            show: true,
            textStyle: {
              fontSize: '14',
              fontWeight: 'normal'
              // color: "rgba(15, 21, 77, 1)"
            },
            formatter: '{b} \n{c} ({d}%)'
          }
        },
        labelLine: {
          normal: {
            show: false
          }
        },
        data: classProbabilities.map(({ class: classId, totalProbability }) => ({
          value: totalProbability,
          name: getClassName(classId)
        })), 
        itemStyle: {
          emphasis: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };

  return (
    <ReactEcharts
      style={{ height: height }}
      option={{
        ...option,
        color: [...color]
      }}
    />
  );
};

export default DoughnutChart;
