import React, { useState } from 'react';
import ChatInput from './components/ChatInput';
import ChatMessage from './components/ChatMessage';
import Sidebar from './components/Sidebar';
import './App.css';  // Assuming CSS is properly linked

function App() {
  const [messages, setMessages] = useState([]);
  const [conversations, setConversations] = useState([{ id: 1, title: 'New Chat 1' }]);
  const [currentConversationId, setCurrentConversationId] = useState(1);

  const handleSendMessage = async (message) => {
    const response = await fetch('/api/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    console.log(data); // Process response

    setMessages(prevMessages => [...prevMessages, { id: Date.now(), content: message, sender: 'user' }]);
  };

  return (
    <div className="chat-app">
      <Sidebar 
        conversations={conversations}
        currentConversationId={currentConversationId}
        onNewChat={() => {/* Logic for creating a new chat */}}
        onSelectConversation={(id) => {/* Logic for selecting a conversation */}}
      />
      <div className="chat-main">
        {messages.map(message => (
          <ChatMessage 
            key={message.id} 
            message={message}
          />
        ))}
        <ChatInput onSendMessage={handleSendMessage} />
      </div>
    </div>
  );
}

export default App;
