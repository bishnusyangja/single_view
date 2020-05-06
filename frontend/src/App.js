import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css'
import {Row, Col, Form, Upload, Button, notification } from 'antd';
import { UploadOutlined } from '@ant-design/icons';


function App() {

    const notify_success = () => {
      notification.open({
        message: 'Register Successful !!',
        description:
          'This is the content of the notification. This is the content of the notification. This is the content of the notification.',
        onClick: () => {
          console.log('Notification Clicked!');
        },
      });
    };

    const submitForm = () => {
        let data = {};
        Request().put('/upload-file/', data)
          .then((response) => {
            console.log("success")
          })
          .catch((error) => {
            console.log("error in quiz submission")
          })
          .finally(() => {
            console.log('finally block at quiz')
        });
    }

  return ( <div style={{margin:'20px'}}>
    <Row>
      <Col span={5} >
         <Form onFinish={submitForm}>
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
