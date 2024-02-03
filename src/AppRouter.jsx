// AppRouter.jsx
import React from 'react';
import Layout from './layouts/Layout';
import NotFound from './pages/NotFound';
import { createBrowserRouter } from "react-router-dom";
import Contact from './pages/Contact';
import Home from './pages/Home';
import Loading from './pages/Loading';

const AppRouter = createBrowserRouter([
    {
        path: "/",
        element: <Layout><Home /></Layout>
    },
    {
        path: "/contact",
        element: <Layout><Contact/></Layout>
    },
    {
        path: "/loading",
        element: <Loading />
    },
    {
        path: "*",
        element: <Layout><NotFound /></Layout>
    }
]);

export default AppRouter;
