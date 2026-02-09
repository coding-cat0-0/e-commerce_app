import {Link, useNavigate} from "react-router-dom";
import authService from "../services/auth.service";
import QueryService from "../services/query.jsx";

function Navbar(){
    const navigate = useNavigate();
    const user = authService.getAuthUser();
    const [searchTerm, setSearchTerm] = useState("")
    const onSubmit = async (e) => {
        // 1. Prevents the browser from refreshing the page
        e.preventDefault(); 

        try {
            // 2. Use the state variable 'searchTerm'
            const response = await QueryService.searchForProducts(searchTerm);
            
            // GraphQL responses usually look like: response.data.data.searchForProducts
            const results = response.data.data.searchForProducts;
            console.log("Search results:", results);
            
        } catch (error) {
            console.error("Search error:", error);
        }
    };

    return (

        <nav className="flex justify-between items-center
         h-16 bg-slate-800 text-white  px-8 fixed top-0 w-full z-50">
            <div className="text-xl font-bold">
                <Link to="/">E-store</Link>
            </div>
            <ul className="flex space-8 items-center">
            <li>
                <Link to="/" className="hover:text-white transition-colors">Home</Link>
            </li>
            <li>
                <Link to="/" className="hover:text-white transition-colors">Deals</Link>
            </li>
            {
            user?.role==='user' && 
            ( <li>
                <Link to="/products" className="hover:text-white transition-colors">Sell</Link>
            </li>
            )
            }
            </ul>
            <form onSubmit={onSubmit} className="flex gap-2">
            <input 
                type="text" 
                className="border p-2 rounded text-black"
                placeholder="Search products..." 
                value={searchTerm} // Ties the input to our state
                onChange={(e) => setSearchTerm(e.target.value)} // Updates state as you type
            />
            <button type="submit" className="bg-blue-500 px-4 py-2 rounded text-white">
                Search
            </button>
            </form>

         </nav>
    )

}
export default Navbar;