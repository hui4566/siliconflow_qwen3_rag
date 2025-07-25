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

## 🔧 故障排除

### 常见问题

1. **API 密钥错误**
   - 确保在 `.env` 文件中正确设置了 `SILICONFLOW_API_KEY`
   - 验证 API 密钥是否有效且有足够的配额

2. **PDF 上传失败**
   - 确保 PDF 文件没有密码保护
   - 检查文件大小是否过大
   - 尝试使用其他 PDF 文件

3. **模型响应慢**
   - 检查网络连接
   - 尝试使用较小的文档
   - 考虑切换到其他模型

4. **OpenAIEmbeddingModelType 错误**
   - 如果遇到 "'Qwen/Qwen3-Embedding-8B' is not a valid OpenAIEmbeddingModelType" 错误
   - 这是因为使用了自定义嵌入模型名称，需要使用 `model_name` 参数而不是 `model` 参数
   - 已在最新版本中修复此问题

5. **生成模型兼容性错误**
   - 如果遇到 "Unknown model 'Qwen/Qwen3-235B-A22B'. Please provide a valid OpenAI model name" 错误
   - 这是因为标准 OpenAI 类不支持第三方模型，需要使用 `OpenAILike` 类
   - 已在最新版本中修复此问题

### 错误日志
如果遇到问题，请查看终端中的错误信息，通常会提供详细的错误描述。

## 🚀 代码质量与可维护性建议

### 📋 单元测试
- **建议添加单元测试**：为核心功能创建测试用例
  - 文档解析功能测试
  - 向量检索功能测试
  - 模型调用功能测试
  - API 连接测试
- **测试框架**：推荐使用 `pytest` 进行单元测试
- **覆盖率**：目标达到 80% 以上的代码覆盖率

### 📝 代码规范
- **类型注解**：为所有函数添加完整的类型注解
- **文档字符串**：遵循 Google 或 NumPy 风格的文档字符串
- **代码格式化**：使用 `black` 和 `isort` 进行代码格式化
- **静态分析**：使用 `mypy` 进行类型检查，`flake8` 进行代码质量检查

### 🔧 架构优化
- **配置管理**：将硬编码的配置项移至配置文件
- **错误处理**：添加更详细的异常处理和用户友好的错误信息
- **日志系统**：实现结构化日志记录，便于问题排查
- **缓存机制**：为文档索引添加缓存，提升性能

### 🔒 安全性
- **API 密钥管理**：确保 API 密钥不被意外提交到版本控制
- **输入验证**：对用户上传的文件进行安全检查
- **依赖安全**：定期更新依赖包，修复安全漏洞

### 📊 性能优化
- **异步处理**：对于大文件处理，考虑使用异步操作
- **内存管理**：优化大文档的内存使用
- **响应时间**：添加进度指示器，改善用户体验

## 📝 更新日志

### v1.0.2 (2025-01-03)
- **修复**: 解决了生成模型兼容性问题
  - 将 `OpenAI` 类替换为 `OpenAILike` 类以支持第三方 OpenAI 兼容 API
  - 添加了 `llama-index-llms-openai-like` 依赖
  - 完全支持硅基流动自定义模型名称（如 Qwen/Qwen3-235B-A22B）
  - 提升了系统稳定性和兼容性

### v1.0.1 (2025-01-03)
- **修复**: 解决了 OpenAIEmbeddingModelType 错误
  - 将嵌入模型配置从 `model` 参数改为 `model_name` 参数
  - 支持使用自定义嵌入模型名称（如 Qwen/Qwen3-Embedding-8B）
  - 提升了与硅基流动 API 的兼容性

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目采用 MIT 许可证。

## 🙏 致谢

- [Streamlit](https://streamlit.io/) - 优秀的 Python Web 应用框架
- [LlamaIndex](https://www.llamaindex.ai/) - 强大的 RAG 框架
- [硅基流动](https://cloud.siliconflow.cn/) - 提供高质量的 AI 模型服务
- [Qwen](https://qwenlm.github.io/) - 优秀的大语言模型

---

**注意**：使用本应用需要有效的硅基流动 API 密钥。请确保遵守相关的使用条款和隐私政策。
