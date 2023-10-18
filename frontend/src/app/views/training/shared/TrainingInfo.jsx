import React, {useState, useEffect} from "react";
import {
    useTheme, 
    Box, 
    Button, 
    Card, 
    styled, 
} from "@mui/material";
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

const TrainingInfo = () => {
    const theme = useTheme();
    const statusMessage = `Sorry, but this feature has not been implemented yet.

    In order to re-train the model please:
    1. Update the audio files in the /dataset folder in the root directory
    2. Modify hyperparameters in /config.json and model in /modules.py
    3. Run the training routine in /trainer.py (with /trainer.ipynb)
    4. Deploy the updated files to the RPI and Jetson modules
    5. Restart pipeline
    `;

    return (
        <Card elevation={3} sx={{ pt: "20px", mb: 3 }}>
            <CardHeader>
                <Title>Work in Progress</Title>
            </CardHeader>
            <Box sx={{ 
                display: "flex", 
                justifyContent: "left", 
                alignItems: "left",
                mb: 2,
                ml: 3,
                whiteSpace: "pre-line"
            }}>
                {statusMessage}
            </Box>
        </Card>
      );
}

export default TrainingInfo;