import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: "http://localhost:5500/",
    headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }
})

export { axiosInstance };