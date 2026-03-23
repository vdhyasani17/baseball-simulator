import styles from '../styles/SimulatePage.module.css'
import { IoMdHome } from "react-icons/io"

function SimulatePage() {
    return (
        <div className={styles.page}>
            <IoMdHome className={styles.homeIcon} onClick={() => window.location.href = "/"} size={40}/>
            <div className={styles.mainContent}>
                <div className={styles.buttonsContainer}>
                    <button className={styles.simulateBtn} onClick={() => window.location.href = "/simulate/game"}><strong>Simulate Game</strong></button>
                    <button className={styles.simulateBtn} onClick={() => window.location.href = "/simulate/season"}><strong>Simulate Season</strong></button>
                </div>
            </div>
        </div>
    )
}

export default SimulatePage;