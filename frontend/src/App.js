import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

   const handleSubmit = (e) => {
        e.preventDefault();
        Request().post('/user/register/', form)
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
   }

  return (
    <div className="App">
    <form onSubmit={handleSubmit}>
      <input type="file" />
      <input type="submit" />
    </form>
    </div>
  );
}

export default App;
