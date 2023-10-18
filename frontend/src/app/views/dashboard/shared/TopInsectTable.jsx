import {
  Avatar,
  Box,
  Card,
  Icon,
  IconButton,
  MenuItem,
  Select,
  styled,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  useTheme,
} from "@mui/material";
import { Paragraph } from "app/components/Typography";
import { useState, useEffect } from "react";

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

const ProductTable = styled(Table)(() => ({
  minWidth: 400,
  whiteSpace: "pre",
  "& small": {
    width: 50,
    height: 15,
    borderRadius: 500,
    boxShadow: "0 0 2px 0 rgba(0, 0, 0, 0.12), 0 2px 2px 0 rgba(0, 0, 0, 0.24)",
  },
  "& td": { borderBottom: "none" },
  "& td:first-of-type": { paddingLeft: "16px !important" },
}));

const Small = styled("small")(({ bgcolor }) => ({
  width: 50,
  height: 15,
  color: "#fff",
  padding: "2px 8px",
  borderRadius: "4px",
  overflow: "hidden",
  background: bgcolor,
  boxShadow: "0 0 2px 0 rgba(0, 0, 0, 0.12), 0 2px 2px 0 rgba(0, 0, 0, 0.24)",
}));

const TopInsectTable = () => {
  const { palette } = useTheme();
  const bgPrimary = palette.primary.main;
  const [classProbabilities, setClassProbabilities] = useState([]);

  useEffect(() => {
    fetch("/api/count/probability")
      .then((response) => response.json())
      .then((data) => setClassProbabilities(Object.entries(data)));
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

  return (
    <Card elevation={3} sx={{ pt: "20px", mb: 3 }}>
      <CardHeader>
        <Title>Total Insect Activity</Title>
      </CardHeader>

      <Box overflow="auto">
        <ProductTable>
          <TableHead>
            <TableRow>
              <TableCell sx={{ px: 3 }} colSpan={4}>
                Class
              </TableCell>
              <TableCell sx={{ px: 0 }} colSpan={2}>
                Total Activity
              </TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            {classProbabilities.map(([classId, totalProbability], index) => (
              <TableRow key={index} hover>
                <TableCell colSpan={4} align="left" sx={{ px: 0, textTransform: "capitalize" }}>
                  <Box display="flex" alignItems="center">
                    <Avatar src={`/assets/images/insects/${classId}.png`} />
                    <Paragraph sx={{ m: 0, ml: 4 }}>{`${getClassName(classId)}`}</Paragraph>
                  </Box>
                </TableCell>

                <TableCell align="left" colSpan={1} sx={{ px: 0, textTransform: "capitalize" }}>
                  <Small bgcolor={bgPrimary}>{totalProbability.toFixed(2)}</Small>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </ProductTable>
      </Box>
    </Card>
  );
};

export default TopInsectTable;
