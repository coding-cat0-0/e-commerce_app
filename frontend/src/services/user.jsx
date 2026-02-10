import axios from 'axios';
import authService from './auth.service';
class userService{

    placeOrder(orderDetails){
        return axios.post(`GQL_URL`, {
            query: `
                mutation PlaceOrder($orderDetails: OrderInput!) {
                    placeOrder(data: $orderDetails) {
                        id
                    }
        }`,
            variables: {
                orderDetails: orderDetails
            }
        }, {
            headers: { 'Authorization': authService.authHeader()}
        });

    }

    cancelOrder(orderId){
        return axios.post(`GQL_URL`, {
            query: `
                mutation CancelOrder($orderId: ID!) {
                    cancelOrder(orderId: $orderId) {
                        id
                    }
        }`,
            variables: {
                orderId: orderId
            }
        }, {
            headers: { 'Authorization': authService.authHeader()}
        });

    }

    getOrders(){
        return axios.post(`GQL_URL`, {
            query: `
                query {
                    orders {
                        id
                        status
                        total
                    }
        }`,
        }, {
            headers: { 'Authorization': authService.authHeader()}
        });
    }

    submitApplication(applicationData){
        return axios.post(`GQL_URL`, {
            query: `
                mutation SubmitApplication($applicationData: ApplicationInput!) {
                    submitApplication(data: $applicationData) {
                        id
                    }
        }`,
            variables: {
                applicationData: applicationData
            }
        }, {    
            headers: { 'Authorization': authService.authHeader()}
        });
    }

    deleteApplication(applicationId){
        return axios.post(`GQL_URL`, {
            query: `
                mutation DeleteApplication($applicationId: ID!) {
                    deleteApplication(applicationId: $applicationId) {
                        id
                    }
                    }`,
                    variables: {
                            applicationId: applicationId
                                }
                     }, {
                                headers: { 'Authorization': authService.authHeader()}
                     });
                }

}
