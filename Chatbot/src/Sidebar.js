import React from 'react';
import NewChatButton from './NewChatButton';

function Sidebar({ conversations, currentConversationId, onNewChat, onSelectConversation }) {
  return (
    <div className="sidebar">
      <NewChatButton onClick={onNewChat} />
      <div className="conversation-list">
        {conversations.map(conv => (
          <div 
            key={conv.id}
            className={`conversation-item ${conv.id === currentConversationId ? 'active' : ''}`}
            onClick={() => onSelectConversation(conv.id)}
          >
            {conv.title}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
