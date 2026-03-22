import React, { useEffect } from 'react';
import styles from '../styles/CreatePlayerForm.module.css';
import { axiosInstance } from '../axios';
import { toast } from 'sonner';

function CreatePlayerForm({ showForm, closeForm}) {
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);

        console.log('Submitting data:', data);
        
        try {
            const response = await axiosInstance.post("/create-batter", data);
            if (response.status === 200) {
                toast.success(`${data.name} has been added successfully!`);
                closeForm();
            } else {
                toast.error('Error creating batter');
                console.log('Error response:', response);
            }
        } catch (error) {
            toast.error('Unable to add player. Please try again.');
            console.error('Error:', error);
        }
    };

    if (!showForm) return null;
    return (
        <div className={styles.backdrop} onClick={closeForm}>
            <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
                <button className={styles.closeButton} onClick={closeForm}>×</button>
                <form className={styles.formContainer} onSubmit={handleSubmit}>
                    <h1>Create Player</h1>

                    <div className={styles.groupsContainer}>
                        <div className={styles.inputGroup}>
                            <div className={styles.inputDiv}>
                                <label htmlFor="player-first-name">Name:</label>
                                <input type="text" id="player-first-name" name="name" required />
                            </div>

                            <div className={styles.inputDiv}>
                                <label htmlFor="k-rate">K Rate:</label>
                                <input type="number" id="k-rate" name="k-rate" step="0.001" min="0" max="1" required defaultValue="0.12"/>
                            </div>

                            <div className={styles.inputDiv}>
                                <label htmlFor="hr-rate">HR Rate:</label>
                                <input type="number" id="hr-rate" name="hr-rate" step="0.001" min="0" max="1" required defaultValue="0.05"/>
                            </div>

                            <div className={styles.inputDiv}>
                                <label htmlFor="slg">SLG:</label>
                                <input type="number" id="slg" name="slg" step="0.001" min="0" max="1" required defaultValue="0.400"/>
                            </div>
                            
                        </div>
                        <div className={styles.inputGroup}>
                            <div className={styles.inputDiv}>
                                <label htmlFor="player-position">Position:</label>
                                <input type="text" id="player-position" name="position" required />
                            </div>

                            <div className={styles.inputDiv}>
                                <label htmlFor="bb-rate">BB Rate:</label>
                                <input type="number" id="bb-rate" name="bb-rate" step="0.001" min="0" max="1" required defaultValue="0.08"/>
                            </div>

                            <div className={styles.inputDiv}>
                                <label htmlFor="avg">AVG:</label>
                                <input type="number" id="avg" name="avg" step="0.001" min="0" max="1" required defaultValue="0.250"/>
                            </div>


                            <div className={styles.inputDiv}>
                                <label htmlFor="babip">BABIP:</label>
                                <input type="number" id="babip" name="babip" step="0.001" min="0" max="1" required defaultValue="0.300"/>
                            </div>
                            
                        </div>
                    </div>

                    <div className={styles.buttonContainer}>
                        <button type="submit" className={styles.submitButton}>Create Player</button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default CreatePlayerForm;