from dotenv import load_dotenv
load_dotenv()



import streamlit as st
st.title("LLM問合せアプリ")
st.write("このアプリは、LLMに対して質問を行うためのアプリケーションです。")

st.write("##### 動作モード1: 法律専門家向けの質問")
st.write("法律に関する質問を入力することで、LLMが回答します。")
st.write("##### 動作モード2: 一般向けの質問")
st.write("一般的な質問を入力することで、LLMが回答します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["法律専門家向けの質問", "一般向けの質問"]
)

st.divider()

if selected_item == "法律専門家向けの質問":
    input_message = st.text_input(label="法律に関する質問を入力してください。")
    text_count = len(input_message)

else:
    input_message = st.text_input(label="一般的な質問を入力してください。")
    text_count = len(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "法律専門家向けの質問":
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

            response = llm([
                SystemMessage(content="あなたは法律の専門家です。"),
                HumanMessage(content=input_message)
            ])

            st.write(response.content)

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

            response = llm([
                SystemMessage(content="あなたは一般的な質問に答えるAIです。"),
                HumanMessage(content=input_message)
            ])

            st.write(response.content)

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")
st.divider()
st.write("##### 注意事項")
st.write("このアプリは、LLMに対して質問を行うためのアプリケーションです。")
st.write("法律専門家向けの質問と一般向けの質問の2つのモードがあります。")