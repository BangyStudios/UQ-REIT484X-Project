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

const PipelineControls = () => {
    const theme = useTheme();

    const [statusMessage, setStatusMessage] = useState("Please select an option")

    const pipelineStart = async () => {
        try {
        const response = await axios.get("/api/pipeline/start")
        setStatusMessage(response.data);
        } catch (error) {
            console.error("Request failed: /api/pipeline/start", error)
            setStatusMessage("Request failed: /api/pipeline/start");
        }
    }

    const pipelineStop = async () => {
        try {
        const response = await axios.get("/api/pipeline/stop")
        setStatusMessage(response.data);
        } catch (error) {
            console.error("Request failed: /api/pipeline/stop", error)
            setStatusMessage("Request failed: /api/pipeline/stop");
        }
    }

    return (
        <Card elevation={3} sx={{ pt: "20px", mb: 3 }}>
            <CardHeader>
                <Title>Pipeline Controls</Title>
            </CardHeader>
        
            <Box sx={{ 
                display: "flex", 
                justifyContent: "center", 
                alignItems: "center",
                mb: 2
            }}>
                <StyledButton variant="contained" color="success" onClick={() => pipelineStart()}>Start</StyledButton>
                <StyledButton variant="contained" color="error" onClick={() => pipelineStop()}>Stop</StyledButton>
            </Box>
            <Box sx={{ 
                display: "flex", 
                justifyContent: "center", 
                alignItems: "center",
                mb: 2
            }}>
                {statusMessage}
            </Box>
        </Card>
      );
}

export default PipelineControls;