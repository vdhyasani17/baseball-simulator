import styles from '../styles/index.module.css'

let totalPlayers = 120;
let totalTeams = 10;
let totalSimulatedGames = 5000; 

function HomePage() {
    return (
        <div className={styles.page}>
            {/* title text */}
            <h1 className={styles.titleText}>Welcome to <strong>Baseball Simulator</strong></h1>

            {/* quick actions */}
            <div className={styles.actions}>
                <h2>Actions</h2>
                <div className="links">
                    <div><a href="/simulate">Simulate</a></div>
                    <div><a href="/manage-entities">Manage Entities</a></div>
                </div>
            </div>

            {/* meta data */}
            <div className={styles.metaData}>
                <h4>Players: {totalPlayers}</h4>
                <h4>Teams: {totalTeams}</h4>
                <h4>Simulated Games: {totalSimulatedGames}</h4>
            </div>
        </div>
    )
}

export default HomePage;