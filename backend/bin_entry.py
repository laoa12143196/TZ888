"""PyInstaller 打包入口：以独立可执行文件方式启动后端。"""

from __future__ import annotations

import os

import uvicorn

# 静态导入，保证 PyInstaller 能正确收集 app 包
from app.main import app as fastapi_app


def main() -> None:
    """启动 uvicorn，参数可通过环境变量覆盖。"""

    host = os.environ.get("BIN_HOST", "127.0.0.1")
    port = int(os.environ.get("BIN_PORT", "8000"))

    uvicorn.run(
        fastapi_app,
        host=host,
        port=port,
        proxy_headers=True,
        forwarded_allow_ips=os.environ.get("BIN_FORWARDED_ALLOW_IPS", "127.0.0.1"),
        log_level=os.environ.get("BIN_LOG_LEVEL", "info"),
    )


if __name__ == "__main__":
    main()
