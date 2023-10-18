import { Card, Grid, styled, useTheme } from "@mui/material";
import { Fragment } from "react";

import TrainingInfo from "./shared/TrainingInfo"


const ContentBox = styled("div")(({ theme }) => ({
  margin: "30px",
  [theme.breakpoints.down("sm")]: { margin: "16px" },
}));

const Title = styled("span")(() => ({
  fontSize: "1rem",
  fontWeight: "500",
  marginRight: ".5rem",
  textTransform: "capitalize",
}));

const SubTitle = styled("span")(({ theme }) => ({
  fontSize: "0.875rem",
  color: theme.palette.text.secondary,
}));

const H4 = styled("h4")(({ theme }) => ({
  fontSize: "1rem",
  fontWeight: "500",
  marginBottom: "16px",
  textTransform: "capitalize",
  color: theme.palette.text.secondary,
}));

const Training = () => {
  const { palette } = useTheme();

  return (
    <Fragment>
      <ContentBox className="TrainingInfo">
        <Grid container spacing={3}>
          <Grid item lg={8} md={8} sm={12} xs={12}>
            <TrainingInfo />
          </Grid>
        </Grid>
      </ContentBox>
    </Fragment>
  );
};

export default Training;
