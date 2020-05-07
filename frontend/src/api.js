import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.crossDomain = true

const getRequestObject = () => {
    let authToken = localStorage.getItem('authToken');
    if (authToken != null && authToken != ''){
        axios.defaults.headers.common['Authorization'] = `Token ${authToken}`;
    }
//    axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

    return axios;
}

export default Request = () => { return {

    get : (url, params) => {
        return getRequestObject().get(url, {params: params});
    },

    post : (url, data) => {
        return getRequestObject().put(url, data);
    },

    put : (url, data) => {
        return getRequestObject().put(url, data);
    },

    patch : (url, data, params) => {
        return getRequestObject().patch(url, data, {params: params});
    },

    del : (url, params) => {
        return getRequestObject().delete(url, {params: params});
    },
}};
