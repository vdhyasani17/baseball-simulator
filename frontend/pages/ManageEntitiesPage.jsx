import { useState } from 'react';
import styles from '../styles/ManageEntities.module.css'
import CreatePlayerForm from '../components/CreatePlayerForm'
import { toast } from 'sonner';
import { IoMdHome } from "react-icons/io";

function ManageEntitiesPage() {
    const [showCreatePlayerForm, setShowCreatePlayerForm] = useState(false);

    const toggleCreatePlayerForm = () => {
        setShowCreatePlayerForm(prev => !prev);
    };

    const notYetImplementedAlert = () => {
        toast.info("This feature is not yet implemented. Stay tuned!");
    }

    return (
        <div className={styles.page}>
            <IoMdHome className={styles.homeIcon} onClick={() => window.location.href = "/"} size={40}/>
            <div className={styles.mainContent}>
                {showCreatePlayerForm && <CreatePlayerForm showForm={showCreatePlayerForm} closeForm={toggleCreatePlayerForm}/>}
                <div className={styles.linksContainer}>
                    <div className="add-player-btn-container">
                        <button className={styles.actionBtn} onClick={toggleCreatePlayerForm}><strong>Add Player</strong></button>
                    </div>
                    <div className="edit-player-btn-container">
                        <button className={styles.actionBtn} onClick={notYetImplementedAlert}><strong>Edit/Delete Player</strong></button>
                    </div>
                    <div className="add-team-btn-container">
                        <button className={styles.actionBtn} onClick={notYetImplementedAlert}><strong>Add Team</strong></button>
                    </div>
                    <div className="edit-team-btn-container">
                        <button className={styles.actionBtn} onClick={notYetImplementedAlert}><strong>Edit/Delete Team</strong></button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ManageEntitiesPage;