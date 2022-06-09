import axios from 'axios'

const LOGIN_URL = '/dj-rest-auth/login/'
const SIGNUP_URL = '/dj-rest-auth/registration/'

const axiosInstance = axios.create({ 
  baseURL: 'http://localhost:8000/'
})

axiosInstance.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

const login = async (body) => {
  const res = await axiosInstance.post(LOGIN_URL, body)
  return res
}

const signup = async (body) => {
  const res = await axiosInstance.post(SIGNUP_URL, body)
  return res 
}

const fetchArticleList = async () => {

  const res = await axiosInstance.get()
  console.log(res)
  return res
}

export {
  login,
  signup,
  fetchArticleList,
}