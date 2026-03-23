import { useState, useEffect } from "react";
import { axiosInstance } from "../axios";
import { toast } from "sonner";
import { IoMdHome } from "react-icons/io";

function SimulatePlayerSeasonPage() {
    const [players, setPlayers] = useState([]);
    const [playerName, setPlayerName] = useState("");
    const [playerId, setPlayerId] = useState("");
    const [playerStats, setPlayerStats] = useState(null);
    useEffect(() => {
        // Fetch player data or set playerId based on user selection
        const fetchBatters = async () => {
            try {
                const response = await axiosInstance.get("/batters");
                setPlayers(response.data.batters);
            } catch (error) {
                toast.error("Error fetching batters");
            }
        };

        fetchBatters();
    }, []);

    const simulatePlayerSeasonStats = async () => {
        try {
            const response = await axiosInstance.get(`/simulate-season/${playerId}`);
            setPlayerName(response.data.name);
            setPlayerStats(response.data.stats);
            toast.success("Player season simulated successfully");
        } catch (error) {
            toast.error("Error simulating player season");
        }
    }

    const mapPlayers = players.map(player => (
        <option key={player._id} value={player._id}>{player.name}</option>
    ));

    return (
        <div>
            <IoMdHome onClick={() => window.location.href = "/"} size={40}/>
            <div>
                <h1>Simulate Player Season</h1>
                <p>This page will allow you to simulate a player's season and see their stats.</p>
                <select value={playerId} onChange={(e) => setPlayerId(e.target.value)}>
                    <option value="">Select a player</option>
                    {mapPlayers}
                </select>
                <button onClick={simulatePlayerSeasonStats} disabled={!playerId}>Simulate Season</button>
                {playerStats && (
                    <div>
                        <h2>{playerName}</h2>
                        <p>{`${playerStats.K} K`}</p>
                        <p>{`${playerStats.BB} BB`}</p>
                        <p>{`${playerStats.HR} HR`}</p>
                        <p>{`${playerStats['1B']} 1B`}</p>
                        <p>{`${playerStats['2B']} 2B`}</p>
                        <p>{`${playerStats['3B']} 3B`}</p>
                        <p>{`${playerStats.FOR}`}</p>
                        <p>{`${playerStats.AVG} / ${playerStats.OBP} / ${playerStats.SLG}`}</p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default SimulatePlayerSeasonPage;