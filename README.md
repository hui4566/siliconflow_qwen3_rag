# 硅基流动 Qwen3 RAG 聊天应用

一个使用 Streamlit、LlamaIndex 和硅基流动 Qwen3 模型构建的RAG（检索增强生成）聊天应用程序。该应用程序允许用户上传 PDF 文档，并通过 AI 驱动的聊天界面与之交互。

## 🚀 功能特性

### 📄 文档处理
- **PDF 文件上传**：支持拖拽或点击上传 PDF 文档
- **实时文档预览**：在侧边栏中预览上传的 PDF 文件
- **自动文档索引**：使用 LlamaIndex 自动处理和索引文档内容

### 💬 聊天界面
- **简洁直观的聊天界面**：类似现代聊天应用的用户体验
- **支持多种消息类型**：文本消息和 AI 响应
- **清除聊天记录功能**：一键清空对话历史
- **可扩展的 AI 推理显示**：展示 AI 的思考过程

### 🤖 AI 模型
- **主要生成模型**：Qwen3-235B-A22B
- **替代生成模型**：DeepSeek-V3
- **嵌入模型**：Qwen3-Embedding-8B
- **实时文档处理**：快速响应用户查询
- **透明 AI 推理显示**：可查看 AI 的推理过程

## 🏗️ 技术架构

该应用程序使用以下技术栈：

- **Streamlit**：用于构建交互式网页界面
- **LlamaIndex**：用于文档处理和 RAG 实现
- **硅基流动 AI**：提供 Qwen3 模型的 API 服务
- **PyPDF2**：用于处理 PDF 文件
- **OpenAI 兼容接口**：通过 OpenAI 格式调用硅基流动 API

## 📦 安装和设置

### 1. 克隆项目
```bash
git clone <repository-url>
cd siliconflow_qwen3_rag
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置 API 密钥

1. 访问 [硅基流动官网](https://cloud.siliconflow.cn/) 注册账户
2. 获取您的 API 密钥
3. 编辑 `.env` 文件，替换 API 密钥：

```env
SILICONFLOW_API_KEY=your_actual_api_key_here
```

### 4. 运行应用
```bash
streamlit run main.py
```

应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

## 🎯 使用方法

### 1. 上传 PDF 文档
- 点击侧边栏的"上传 PDF"区域
- 选择您要分析的 PDF 文件
- 等待文档处理完成

### 2. 开始对话
- 在底部聊天输入框中输入您的问题
- AI 将基于上传的文档内容回答您的问题
- 可以查看 AI 的推理过程（点击"AI 推理过程"展开）

### 3. 管理对话
- 使用"清除聊天"按钮清空对话历史
- 可以随时上传新的 PDF 文档
- 支持切换不同的 AI 模型

## ⚙️ 配置选项

### 模型选择
- **生成模型**：
  - Qwen3-235B-A22B（推荐）
  - DeepSeek-V3
- **嵌入模型**：
  - Qwen3-Embedding-8B

### 高级设置
可以在代码中调整以下参数：
- `temperature`：控制回答的创造性（默认：0.7）
- `max_tokens`：最大回答长度（默认：2048）
- `similarity_top_k`：检索相关文档数量（默认：5）

### 错误日志
如果遇到问题，请查看终端中的错误信息，通常会提供详细的错误描述。

## 📄 许可证

本项目采用 MIT 许可证。

