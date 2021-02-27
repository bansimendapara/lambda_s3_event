// import logo from './logo.svg';
import React, { useState, useEffect } from 'react'
import './App.css';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import * as ReactBootStrap from 'react-bootstrap';
import axios from 'axios';

const App = () => {

  const [s3, setChange] = useState([])
  const [loading, setLoading] = useState(false);

  const getData = async () => {
    try {
      const data = await axios.get("https://4uylvx38ac.execute-api.us-east-1.amazonaws.com/prod/s3change");
      console.log(data.data)
      setChange(data.data);
      setLoading(true);
    } catch (e) {
      console.log(e)
    }
  };

  useEffect(() => {
    getData();
  }, []);

  const s3Column = [
    // { dataField: "RequestID", text: "Request ID" },
    { dataField: "Date", text: "Date", sort: true },
    { dataField: "Time", text: "Time", sort: true },
    { dataField: "EventType", text: "Event Type" },
    { dataField: "Object", text: "Object" },
    { dataField: "Size", text: "Size" }
  ]


  return (
    <div className="App">
      {loading ? (<BootstrapTable
        // bootstrap4
        keyField="RequestID"
        data={s3}
        columns={s3Column}
        pagination={paginationFactory()}
        striped
        hover
      />
      ) : (
          <ReactBootStrap.Spinner animation="border" />
        )}

    </div>
  );

}

export default App;
