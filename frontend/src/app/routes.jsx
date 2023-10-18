import { lazy } from "react";
import { Navigate } from "react-router-dom";
import AuthGuard from "./auth/AuthGuard";
import { authRoles } from "./auth/authRoles";
import Loadable from "./components/Loadable";
import MatxLayout from "./components/MatxLayout/MatxLayout";
import materialRoutes from "app/views/material-kit/MaterialRoutes";

// session pages
const NotFound = Loadable(lazy(() => import("app/views/sessions/NotFound")));
const JwtLogin = Loadable(lazy(() => import("app/views/sessions/JwtLogin")));
const JwtRegister = Loadable(lazy(() => import("app/views/sessions/JwtRegister")));
const ForgotPassword = Loadable(lazy(() => import("app/views/sessions/ForgotPassword")));

// Echart page
const AppEchart = Loadable(lazy(() => import("app/views/charts/echarts/AppEchart")));

// Dashboard page
const Dashboard = Loadable(lazy(() => import("app/views/dashboard/Dashboard")));

// Dashboard page
const Training = Loadable(lazy(() => import("app/views/training/Training")));

// Dataset page
const Dataset = Loadable(lazy(() => import("app/views/dataset/Dataset")));

// Settings page
const Settings = Loadable(lazy(() => import("app/views/settings/Settings")));

const routes = [
    {
        element: (
            <AuthGuard>
            <MatxLayout />
            </AuthGuard>
            ),
            children: [
                ...materialRoutes,
                // Dashboard route
                {
                    path: "/dashboard",
                    element: <Dashboard />,
                    auth: authRoles.admin
                },

                // Training route
                {
                    path: "/training",
                    element: <Training />,
                    auth: authRoles.admin
                },

                // Dataset route
                {
                    path: "/dataset",
                    element: <Dataset />,
                    auth: authRoles.admin
                },
                
                // Settings route
                {
                    path: "/settings",
                    element: <Settings />,
                    auth: authRoles.admin
                }, 
                
                // E-Chart rooute
                {
                    path: "/charts/echarts",
                    element: <AppEchart />,
                    auth: authRoles.editor
                }
            ]
        },
        
        // session pages route
        { path: "/session/404", element: <NotFound /> },
        { path: "/session/signin", element: <JwtLogin /> },
        { path: "/session/signup", element: <JwtRegister /> },
        { path: "/session/forgot-password", element: <ForgotPassword /> },
        
        { path: "/", element: <Navigate to="dashboard" /> },
        { path: "*", element: <NotFound /> }
    ];
    
    export default routes;
    