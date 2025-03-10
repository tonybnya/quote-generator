import { useEffect, useState } from "react";
import quoteLogo from "/quote.svg";
import "./App.css";
import Blockquote from "./components/Blockquote";
import Spinner from "./components/Spinner";

const App = () => {
  // state to store fetched data
  const [data, setData] = useState(null);
  // state to store any errors
  const [error, setError] = useState(null);
  // state to control loading state
  const [loading, setLoading] = useState(false);

  const API_URL = import.meta.env.VITE_API_URL;
  console.log(API_URL);

  // effect to fetch the data when the component mounts
  useEffect(() => {
    fetchData();
  }, []); // empty dependency object ensures the effect runs once on mount

  // function to fetch data
  const fetchData = async () => {
    // start loading
    setLoading(true);

    try {
      // make a GET request using the Fetch API
      const response = await fetch(API_URL);

      // check if response is successfull (status code 200-299)
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // parse the JSON data from the response
      const result = await response.json();

      // update the state with the fetched data
      setData(result);
      // log the fetched data in the console
      console.log(result);
    } catch (error) {
      // update the error state
      setError(error.message);
      console.error("Error fetching data:", error.message);
    } finally {
      // end loading
      setLoading(false);
    }
  };

  return (
    <>
      <div className="flex flex-col items-center justify-center pb-4">
        <img src={quoteLogo} className="logo" alt="quote logo" />
        <h1 className="tracking-tighter">Quote Generator</h1>
        <a target="_blank" href="https://github.com/tonybnya/quote-generator">
          <i className="fa-brands fa-github"></i>
        </a>
      </div>
      {error ? (
        <p className="text-red-500">Error: {error}</p>
      ) : loading ? (
        <Spinner />
      ) : data ? (
        <Blockquote author={data.author} quote={data.quote} />
      ) : (
        <p>No quote available.</p>
      )}
      <button className="pt-8" onClick={fetchData}>
        Generate
      </button>
    </>
  );
};

export default App;
