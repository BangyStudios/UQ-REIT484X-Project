import axios from 'axios';
import { useState, useEffect } from 'react';

import { Box, Card, Grid, Icon, IconButton, styled, Tooltip } from '@mui/material';
import { Small } from 'app/components/Typography';

const StyledCard = styled(Card)(({ theme }) => ({
  display: 'flex',
  flexWrap: 'wrap',
  alignItems: 'center',
  justifyContent: 'space-between',
  padding: '24px !important',
  background: theme.palette.background.paper,
  [theme.breakpoints.down('sm')]: { padding: '16px !important' },
}));

const ContentBox = styled(Box)(({ theme }) => ({
  display: 'flex',
  flexWrap: 'wrap',
  alignItems: 'center',
  '& small': { color: theme.palette.text.secondary },
  '& .icon': { opacity: 0.6, fontSize: '44px', color: theme.palette.primary.main },
}));

const Heading = styled('h6')(({ theme }) => ({
  margin: 0,
  marginTop: '4px',
  fontSize: '14px',
  fontWeight: '500',
  color: theme.palette.primary.main,
}));

const StatCards = () => {
  const [cardList, setCardList] = useState([
    { name: 'Total Events', amount: 0, icon: 'group' },
    { name: 'Total Datapoints', amount: 0, icon: 'group'}
  ]);

  const fetchTotalEvents = () => {
    axios.get("/api/stats/count/events")
      .then(response => {
        const totalEventsContent = response.data[0]['COUNT(DISTINCT timestamp)'];
        setCardList(prevList => [
          { ...prevList[0], amount: totalEventsContent },
          prevList[1],
        ]);
      })
      .catch(error => {
        setCardList(prevList => [
          { ...prevList[0], amount: "Failed to load /stats/count/events" },
          prevList[1],
        ]);
        console.error("There was an error fetching the total events:", error);
      });
  };

  const fetchTotalDatapoints = () => {
    axios.get("/api/stats/count/datapoints")
      .then(response => {
        const totalDatapointsContent = response.data[0]['COUNT(*)'];
        setCardList(prevList => [
          prevList[0],
          { ...prevList[1], amount: totalDatapointsContent },
        ]);
      })
      .catch(error => {
        setCardList(prevList => [
          prevList[0],
          { ...prevList[1], amount: "Failed to load /stats/count/datapoints" },
        ]);
        console.error("There was an error fetching the total datapoints:", error);
      });
  }

    useEffect(() => {
      fetchTotalEvents(setCardList);
      fetchTotalDatapoints(setCardList);
    }, []);

    const fetchAll = () => {
      fetchTotalEvents(setCardList);
      fetchTotalDatapoints(setCardList);
    }

  return (
    <Grid container spacing={3} sx={{ mb: '24px' }}>
      {cardList.map((item, index) => (
        <Grid item xs={12} md={6} key={index}>
          <StyledCard elevation={6}>
            <ContentBox>
              <Icon className="icon">{item.icon}</Icon>
              <Box ml="12px">
                <Small>{item.name}</Small>
                <Heading>{item.amount}</Heading>
              </Box>
            </ContentBox>

            <Tooltip title="Refresh" placement="top">
              <IconButton onClick={() => fetchAll()}>
                <Icon>refresh</Icon>
              </IconButton>
            </Tooltip>
          </StyledCard>
        </Grid>
      ))}
    </Grid>
  );
};

export default StatCards;
