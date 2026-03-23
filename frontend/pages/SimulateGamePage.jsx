import { axiosInstance } from "../axios";
import { toast } from "sonner";

function SimulateGamePage() {
    const simulateGame = async () => {
        try {
            const response = await axiosInstance.get("/simulate-game");
        } catch (error) {
            toast.error("Error simulating game:", error);
        }
    }
    return (
        <div>
            Simulate Game Page
        </div>
    )
}

export default SimulateGamePage;