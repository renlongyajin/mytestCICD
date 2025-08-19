# 使用官方的 Python 3.9 镜像作为基础
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到工作目录
COPY requirements.txt .

# 安装 pytest
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码和测试文件
COPY . .

# 保持容器运行，以便在 CI 管道中使用
CMD ["/bin/bash"]