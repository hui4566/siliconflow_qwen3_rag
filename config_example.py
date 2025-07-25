# 配置示例文件
# 复制此文件为 config.py 并根据需要修改设置

# 硅基流动 API 配置
SILICONFLOW_CONFIG = {
    "api_base": "https://api.siliconflow.cn/v1",
    "timeout": 60,  # 请求超时时间（秒）
    "max_retries": 3,  # 最大重试次数
}

# 模型配置
MODEL_CONFIG = {
    "generative_models": [
        "Qwen/Qwen3-235B-A22B",
        "deepseek-ai/DeepSeek-V3",
        "Qwen/Qwen2.5-72B-Instruct",
        "meta-llama/Meta-Llama-3.1-405B-Instruct"
    ],
    "embedding_models": [
        "Qwen/Qwen3-Embedding-8B",
        "BAAI/bge-large-zh-v1.5",
        "text-embedding-3-large"
    ],
    "default_generative": "Qwen/Qwen3-235B-A22B",
    "default_embedding": "Qwen/Qwen3-Embedding-8B"
}

# LLM 参数配置
LLM_PARAMS = {
    "temperature": 0.7,
    "max_tokens": 2048,
    "top_p": 0.9,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

# RAG 配置
RAG_CONFIG = {
    "similarity_top_k": 5,  # 检索的相关文档数量
    "chunk_size": 1024,     # 文档分块大小
    "chunk_overlap": 200,   # 分块重叠大小
    "response_mode": "compact"  # 响应模式
}

# Streamlit 界面配置
UI_CONFIG = {
    "page_title": "硅基流动 Qwen3 RAG 聊天",
    "page_icon": "🤖",
    "layout": "wide",
    "sidebar_width": 300,
    "max_file_size": 200,  # MB
    "supported_formats": ["pdf"]
}

# 日志配置
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "app.log"
}
