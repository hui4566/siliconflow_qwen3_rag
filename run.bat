@echo off
echo 启动硅基流动 Qwen3 RAG 聊天应用...
echo.

:: 检查是否存在虚拟环境
if exist "venv\Scripts\activate.bat" (
    echo 激活虚拟环境...
    call venv\Scripts\activate.bat
) else (
    echo 未找到虚拟环境，使用系统Python环境
)

:: 检查是否存在 .env 文件
if not exist ".env" (
    echo 警告: 未找到 .env 文件，请确保已配置 SILICONFLOW_API_KEY
    echo.
)

:: 安装依赖（如果需要）
echo 检查依赖包...
pip install -r requirements.txt --quiet

:: 启动应用
echo.
echo 启动 Streamlit 应用...
echo 应用将在浏览器中自动打开: http://localhost:8501
echo.
echo 按 Ctrl+C 停止应用
echo.

streamlit run main.py

pause
