import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: "http://localhost:5000/",
    headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }
})

export { axiosInstance };