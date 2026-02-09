import axios from 'axios';
import { authHeader } from './auth.service.jsx';

class HomeDashbaordService {

    getAllProducts(){
        return axios.get('GQL_URL',{
            query:`
            query getAllProducts{
            allProducts{
                id
                name
                price
                description
                image
                category}
            }`
        }, {
            headers: authHeader()
        });

    }


}