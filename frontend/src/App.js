import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";
import Dashboard from "./Dashboard";
import AdminDashboard from "./AdminDashboard";
import ThreatHeatmap from "./ThreatHeatmap";
import RetrieveLogs from "./RetrieveLogs";
import Chatbot from "./Chatbot";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/admin" element={<AdminDashboard />} />
                <Route path="/threats" element={<ThreatHeatmap />} />
                <Route path="/retrieve-logs" element={<RetrieveLogs />} />
                <Route path="/chatbot" element={<Chatbot />} />
            </Routes>
        </Router>
    );
}

export default App;