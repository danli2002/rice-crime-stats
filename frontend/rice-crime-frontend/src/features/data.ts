import axios from 'axios'



export const getData = async() => {
    
    let response = await axios.get('http://localhost:5000/flask/hello')
    return response.data

}
