import streamlit as st
import os
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai_like import OpenAILike
from dotenv import load_dotenv
import tempfile
import shutil
import base64
import io
import re

# Load environment variables
load_dotenv()

def run_rag_completion(
    documents,
    query_text: str,
    embedding_model: str = "Qwen/Qwen3-Embedding-8B",
    generative_model: str = "Qwen/Qwen3-235B-A22B"
) -> str:
    """使用硅基流动模型运行RAG完成任务。"""
    # 配置硅基流动的LLM
    llm = OpenAILike(
        model=generative_model,
        api_key=os.getenv("SILICONFLOW_API_KEY"),
        api_base="https://api.siliconflow.cn/v1",
        temperature=0.7,
        max_tokens=2048,
        is_chat_model=True,
        is_function_calling_model=False
    )

    # 配置硅基流动的嵌入模型
    embed_model = OpenAIEmbedding(
        model_name=embedding_model,
        api_key=os.getenv("SILICONFLOW_API_KEY"),
        api_base="https://api.siliconflow.cn/v1"
    )
    
    Settings.llm = llm
    Settings.embed_model = embed_model
    
    # 创建索引并查询
    index = VectorStoreIndex.from_documents(documents)
    response = index.as_query_engine(similarity_top_k=5).query(query_text)
    
    return str(response)

def display_pdf_preview(pdf_file):
    """在侧边栏显示PDF预览。"""
    try:
        # 显示PDF信息
        st.sidebar.subheader("PDF 预览")
        
        # 将PDF转换为base64用于显示
        base64_pdf = base64.b64encode(pdf_file.getvalue()).decode('utf-8')
        
        # 使用HTML iframe显示PDF
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
        
        return True
    except Exception as e:
        st.sidebar.error(f"预览PDF时出错: {str(e)}")
        return False

def format_reasoning_response(thinking_content):
    """格式化助手内容，移除思考标签。"""
    return (
        thinking_content.replace("<think>\n\n</think>", "")
        .replace("<think>", "")
        .replace("</think>", "")
    )

def display_assistant_message(content):
    """显示助手消息，如果存在思考内容则展示。"""
    pattern = r"<think>(.*?)</think>"
    think_match = re.search(pattern, content, re.DOTALL)
    if think_match:
        think_content = think_match.group(0)
        response_content = content.replace(think_content, "")
        think_content = format_reasoning_response(think_content)
        with st.expander("AI 推理过程"):
            st.markdown(think_content)
        st.markdown(response_content)
    else:
        st.markdown(content)

def main():
    """主函数，运行Streamlit应用程序。"""
    st.set_page_config(page_title="硅基流动 Qwen3 RAG 聊天", layout="wide")
    
    # 初始化会话状态
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "docs_loaded" not in st.session_state:
        st.session_state.docs_loaded = False
    if "temp_dir" not in st.session_state:
        st.session_state.temp_dir = None
    if "current_pdf" not in st.session_state:
        st.session_state.current_pdf = None
    
    # 标题和按钮
    col1, col2 = st.columns([4, 1])
    with col1:
        # 创建带有图标的标题
        title_html = """
        <div style="display: flex; align-items: center; gap: 10px;">
            <h1 style="margin: 0;">🤖 RAG Chat with Qwen3 & LlamaIndex</h1>
        </div>
        """
        st.markdown(title_html, unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ 清除聊天"):
            st.session_state.messages = []
            st.session_state.docs_loaded = False
            if st.session_state.temp_dir:
                shutil.rmtree(st.session_state.temp_dir)
                st.session_state.temp_dir = None
            st.session_state.current_pdf = None
            st.rerun()
    
    st.caption("由硅基流动 AI 驱动")
    
    # 侧边栏配置
    with st.sidebar:
        st.markdown("### 🚀 硅基流动 Qwen3 RAG")
        
        # 模型选择
        generative_model = st.selectbox(
            "生成模型",
            ["Qwen/Qwen3-235B-A22B", "deepseek-ai/DeepSeek-V3"],
            index=0
        )
        
        embedding_model = st.selectbox(
            "嵌入模型",
            ["Qwen/Qwen3-Embedding-8B"],
            index=0
        )
        
        st.divider()
        
        # PDF文件上传
        st.subheader("📄 上传 PDF")
        uploaded_file = st.file_uploader(
            "选择一个PDF文件",
            type="pdf",
            accept_multiple_files=False
        )
        
        # 处理PDF上传和处理
        if uploaded_file is not None:
            if uploaded_file != st.session_state.current_pdf:
                st.session_state.current_pdf = uploaded_file
                try:
                    if not os.getenv("SILICONFLOW_API_KEY"):
                        st.error("缺少硅基流动 API 密钥")
                        st.stop()
                    
                    # 为PDF创建临时目录
                    if st.session_state.temp_dir:
                        shutil.rmtree(st.session_state.temp_dir)
                    st.session_state.temp_dir = tempfile.mkdtemp()
                    
                    # 将上传的PDF保存到临时目录
                    file_path = os.path.join(st.session_state.temp_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    with st.spinner("正在加载PDF..."):
                        # 从临时目录加载文档
                        documents = SimpleDirectoryReader(st.session_state.temp_dir).load_data()
                        st.session_state.docs_loaded = True
                        st.session_state.documents = documents
                        st.success("✓ PDF 加载成功")
                        
                        # 显示PDF预览
                        display_pdf_preview(uploaded_file)
                except Exception as e:
                    st.error(f"错误: {str(e)}")
    
    # 显示聊天消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                display_assistant_message(message["content"])
            else:
                st.markdown(message["content"])
    
    # 聊天输入
    if prompt := st.chat_input("询问您的PDF内容..."):
        if not st.session_state.docs_loaded:
            st.error("请先上传PDF文件")
            st.stop()
        
        # 添加用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 生成响应
        with st.chat_message("assistant"):
            with st.spinner("正在思考..."):
                try:
                    response = run_rag_completion(
                        st.session_state.documents,
                        prompt,
                        embedding_model,
                        generative_model
                    )
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    display_assistant_message(response)
                except Exception as e:
                    st.error(f"错误: {str(e)}")

if __name__ == "__main__":
    main()
