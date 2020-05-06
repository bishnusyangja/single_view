import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css'
import {Row, Col, Form, Upload, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';


function App() {
  return ( <div style={{margin:'20px'}}>
    <Row>
      <Col span={5} >
         <Form>
        <Form.Item> <Upload >
            <Button>
              <UploadOutlined /> Upload
            </Button>
          </Upload>
        </Form.Item>
        <Form.Item>  <Button type="primary" htmlType="submit">  Submit </Button> </Form.Item>
      </Form>
       </Col>
      <Col span={1} > </Col>
      <Col span={5} > Hello World </Col>
   </Row>
</div>
  );
}

export default App;
