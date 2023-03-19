import openai
import streamlit as st

# 设置OpenAI API密钥
openai.api_key = st.text_input("Enter your OpenAI API key", type="password")

# Streamlit界面
st.title("GPT-3 Demo")
prompt = st.text_input("Enter a prompt")
temperature = st.slider("Temperature", 0.0, 1.0, step=0.1)
max_tokens = st.slider("Max tokens", 10, 2048, step=10)
stop_sequence = st.text_input("Stop sequence")

# 生成回答
response = st.empty()
if st.button("Generate"):
    try:
        # 调用OpenAI API生成回答
        completions = openai.Completion.create(
            engine="davinci", prompt=prompt, max_tokens=max_tokens, temperature=temperature, stop=stop_sequence
        )
        message = completions.choices[0].text
        response.text(message)
    except Exception as e:
        response.text(f"Error: {e}")

# 沿用之前的对话
if st.button("Continue conversation"):
    prompt = f"{prompt.strip()} {response.text_input('You', key='input')} {stop_sequence}"
    try:
        completions = openai.Completion.create(
            engine="davinci", prompt=prompt, max_tokens=max_tokens, temperature=temperature, stop=stop_sequence
        )
        message = completions.choices[0].text
        response.text(message)
    except Exception as e:
        response.text(f"Error: {e}")
