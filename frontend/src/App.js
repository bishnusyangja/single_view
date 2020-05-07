import React from 'react';
import {useState, useEffect} from 'react';
import './App.css';
import 'antd/dist/antd.css'
import {Row, Col, Form, Upload, Button, Table, Pagination, notification } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import Request from './api';


function App() {

    let pagination = {page: 1, pageSize: 50};

    const [file_data, setFile] = useState({file: null});

    const [data, setData] = useState({results: [], count: 0});

    const get_data = (page, pageSize) => {
        Request().get('/work-single/', {page: page, page_size: pageSize})
          .then((response) => {
            setData(response.data);
          })
          .catch((error) => {
            console.log("error");
          })
          .finally(() => {
            console.log('finally block')
        });
    }

    useEffect(() => {
        get_data(pagination.page, pagination.pageSize);
    }, []);


    const notify_success = () => {
      notification.open({
        message: 'Upload Successful !!!',
        description:
          'The action completed successfully.',
        onClick: () => {
          console.log('Notification Clicked!');
        },
      });
    };

    const notify_error = () => {
      notification.open({
        message: 'Error ',
        description:
          'Something went wrong with server or your file.',
        onClick: () => {
          console.log('Notification Clicked!');
        },
      });
    };

    const submitForm = () => {
        let formData = new FormData();
        console.log(file_data.file);
        formData.append("file", file_data.file);
        console.log(formData);
        Request().put('/upload-file/', formData)
          .then((response) => {
            console.log("success");
            notify_success();
          })
          .catch((error) => {
            console.log("error")
            notify_error();
          })
          .finally(() => {
            console.log('finally block')
        });
    }

    const columns = [
        {
        title: 'SN',
        dataIndex: '',
        key: 'sn',
        render: (text, record, index) =>  (data.page - 1) * data.pageSize + index+1,
      },
      {
        title: 'Title',
        dataIndex: 'title',
        key: 'title',
      },
      {
        title: 'Contributors',
        dataIndex: 'contributors',
        key: 'contributors',
      },
      {
        title: 'ISWC',
        dataIndex: 'iswc',
        key: 'iswc',
      },
      {
        title: 'ID',
        dataIndex: 'item_id',
        key: 'item_id',
      },
    ]

    const onPageChange = (page, pageSize) => {
        get_data(page, pageSize);
    }

    const fileUploadChange = (file, fileList) => {
        setFile({file: file.file});
    }

//    const customReq = () => false;

  return ( <div style={{margin:'20px'}}>
    <Row> <div style={{marginBottom: '100px', align: 'center'}}><h1 >Welcome to Musical Work App</h1></div> </Row>

    <Row>
      <Col span={4} >
         <Form onFinish={submitForm}>
        <Form.Item> <Upload  beforeUpload={() => false} onChange={fileUploadChange}>
            <Button>
              <UploadOutlined
                /> Select File
            </Button>
          </Upload>
        </Form.Item>
        <Form.Item>  <Button type="primary" htmlType="submit">  Upload </Button> </Form.Item>
      </Form>
       </Col>
      <Col span={3} > </Col>
      <Col span={12} > <h2>Musical Work Listing </h2> <a href="http://localhost:8000/work-single/?download=download">
           Download All Data </a>
        {data && <Table dataSource={data.results} columns={columns} pagination={false}/>}
                    <Pagination defaultCurrent={1}
                              pageSize={pagination.pageSize}
                              total={data.count}
                              onChange={onPageChange}/>
      </Col>
   </Row>
</div>
  );
}

export default App;
