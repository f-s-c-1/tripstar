"""后端启动脚本，自动读取 .env 中的 HOST/PORT 配置"""
import os
from pathlib import Path

# 加载 .env
env_file = Path(__file__).parent / ".env"
if env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(env_file)

import uvicorn

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "6003"))

    uvicorn.run(
        "app.api.main:app",
        host=host,
        port=port,
        reload=True,
    )
