import './App.css';
import React, { useEffect, useState } from 'react';
import { Link, BrowserRouter as Router, Route } from "react-router-dom";
import axios from 'axios'

const PersonPage = ({ match }) => {
  const {
    params: { personId },
  } = match;
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState();

  /*useEffect(() => {
  }, [personId]);
*/

  return (
    <>
      {(
        <>
        <div>{personId == 1 ? 
         <form>
          <label>
            Enter keyword:
            <input type="text" name="keyword" />
          </label>
          <input type="submit" value="Submit" />
         </form>
          :
        <form>
          <label>
            Name:
            <input type="text" name="name" />
          </label>
          <input type="submit" value="Submit" />
         </form>}</div>
          <Link to="/">Back to homepage</Link>
        </>
      )}
    </>
  );
};

const HomePage = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState();

  useEffect(() => {
        let options = [
          {name: 'Search by keyword'}, {name: 'search by telephone number'}
        ]

        setData(options)
        setIsLoading(false);  
  }, []);

  return (
    <>
      {!isLoading &&
        data.map((person, index) => {
          return (
            <h5 key={index}>
              <Link to={`/${index + 1}`}>{person.name}</Link>
            </h5>
          );
        })}
    </>
  );
};

const App = () => {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/flask/hello').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <>
      <Router>
        <Route exact path="/" component={HomePage} />
        <Route path="/:personId" component={PersonPage} />
      </Router>
    </>
  );
};

export default App;