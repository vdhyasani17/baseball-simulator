import { useState } from 'react';
import styles from '../styles/manage-entities.module.css'
import CreatePlayerForm from '../components/CreatePlayerForm'

function ManageEntitiesPage() {
    const [showCreatePlayerForm, setShowCreatePlayerForm] = useState(false);

    const toggleCreatePlayerForm = () => {
        setShowCreatePlayerForm(prev => !prev);
    };

    return (
        <div className={styles.page}>
            {showCreatePlayerForm && <CreatePlayerForm showForm={showCreatePlayerForm} closeForm={toggleCreatePlayerForm}/>}
            <div className={styles.linksContainer}>
                <div className="add-player-btn-container">
                    <button className={styles.actionBtn} onClick={toggleCreatePlayerForm}><strong>Add Player</strong></button>
                </div>
                <div className="edit-player-btn-container">
                    <button className={styles.actionBtn}><strong>Edit/Delete Player</strong></button>
                </div>
                <div className="add-team-btn-container">
                    <button className={styles.actionBtn}><strong>Add Team</strong></button>
                </div>
                <div className="edit-team-btn-container">
                    <button className={styles.actionBtn}><strong>Edit/Delete Team</strong></button>
                </div>
            </div>
        </div>
    )
}

export default ManageEntitiesPage;