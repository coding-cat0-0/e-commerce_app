import React, { useState, useRef } from "react";
import { Form, Input, Button as CheckButton } from "react-validation";
import { isEmail } from "validator";
import {useForm} from "react-hook-form";
import AuthService from "../services/auth.service";
import { AuthContext } from "../context/Auth.Context";
import { useContext } from "react";

const Login = () => {
    const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm();
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");
    const form = useRef();
    const checkBtn = useRef();
    const { setLoggedIn } = useContext(AuthContext);
    const navigate = useNavigate();
    const onSubmit = async (data) => {
        try {
            await AuthService.login(data.email, data.password);
            setLoggedIn(true);
            //write navigation logic here;
            alert("Login successful!");
        } catch (error) {
            setLoggedIn(false);
            alert("Login failed: " + error.message);
        }
    }

    return(
 <div className="max-w-md m-auto mt-40 p-9  hover:scale-110 hover:scale-[1.02] transition-all duration-500 bg-white rounded-lg shadow-md">
            <h2 className="text-3xl ml-20 mb-5 font-sans font-extrabold text-gray-800">Create account</h2>
            <form onSubmit={handleSubmit(onSubmit)} ref={form}>
                <div className="mb-4">
                    <label htmlFor="email" className="block text-gray-700
                     font-bold mb-2">Email</label>
                    <input 
                    type="text"
                    placeholder="Enter email"
                    className="shadow appearance-none border-none placeholder-gray-500 bg-gray-100 rounded-xl 
                    w-full py-4 px-3 text-gray-700 leading-tight focus:outline-none "
                    {...register("email", { required: "Email is required" })}
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="password" className="block text-gray-700
                     font-bold mb-2">Password</label>
                    <input 
                    type="text"
                    placeholder="Enter password"
                    className="shadow appearance-none border-none placeholder-gray-500 bg-gray-100 rounded-xl 
                    w-full py-4 px-3 text-gray-700 leading-tight focus:outline-none"
                    {...register("password", { required: "Password is required" })}
                    />
                    
                </div>
                <button className="w-40 bg-green-500 mt ml-30 hover:bg-blue-700 rounded-full text-white
                font-bold py-4 px-4 "
                disabled={loading}>
                    {loading && <span className="animate-spin mr-2">...</span>}
                    <span>Signin</span>
                </button>
                {message && (
                    <div className="mt-4 p-2 bg-red-100 text-red-700 text-center
                     rounded">
                        {message}
                        </div>
                )}
            </form>
        </div>
    )}
export default Login;