import streamlit as st
import streamlit.components.v1 as components

def render_chatbot():
    """
    Renders the chatbot in the sidebar using a standard Streamlit expander.
    This provides a reliable, simple UI.
    """
    chat_url = "https://ashumishra123.app.n8n.cloud/webhook/9cb94792-2091-40a7-97f0-1a7c0265dfe3/chat"
    
    # Standard n8n chat embed code
    # This uses the official n8n chat library to render the widget
    chat_embed_code = f"""
    <div id="n8n-chat"></div>
    <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
    <script type="module">
        import {{ createChat }} from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';
        
        createChat({{
            webhookUrl: '{chat_url}',
            mode: 'window',
            target: '#n8n-chat',
            showWelcomeScreen: true,
            initialMessages: [
                'Hi there! 👋',
                'How can I help you with your flight booking today?'
            ],
            i18n: {{
                en: {{
                    title: 'SkyConnect Assistant',
                    subtitle: 'Ask me anything about flights',
                }}
            }}
        }});
    </script>
    """
    
    # Inject the embed code
    # We place it in the sidebar so it's always accessible without scrolling the main page
    with st.sidebar:
        st.markdown("---")
        st.header("🤖 AI Assistant")
        # We use height=550 to allow the chat window to expand within the iframe in the sidebar
        components.html(chat_embed_code, height=550)
