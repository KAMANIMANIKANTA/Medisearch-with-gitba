import React from 'react';

function NewChatButton({ onClick }) {
  return (
    <button onClick={onClick} className="new-chat-button">
      + New Chat
    </button>
  );
}

export default NewChatButton;
