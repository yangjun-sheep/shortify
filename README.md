# 短链接服务

## 项目介绍

本服务提供3个接口

1. 生成短链接
2. 根据短链接获得原链接
3. 短链接跳转

## 技术栈

- Python 3.12
- FastAPI
- AMIS

## 运行

```bash
pip install -r requirements.txt
uvicorn app.main:app --host=0.0.0.0 --port=9002 --reload
```

## 访问

前端页面：http://127.0.0.1:9002
接口文档：http://127.0.0.1:9002/docs
