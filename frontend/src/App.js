import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css';

import {Button} from 'antd';

function App() {

   const handleSubmit = (e) => {
        e.preventDefault();
        Request().put('/file-upload/', {})
        .then(function (response) {
             console.log("success");
          })
          .catch(function (err) {
            console.log(err.response);
          })
          .finally(function () {
            console.log('finally block')
        });
    };

  return (
    <div className="App" style={{margin:'20px'}}>
    <form>
        <input type="file" />
        <input type="submit" value="Submit"/>
    </form>

    </div>
  );
}

export default App;
