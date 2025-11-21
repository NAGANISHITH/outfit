// DOM Elements
const analysisForm = document.getElementById('analysisForm');
const loading = document.getElementById('loading');
const fileInput = document.getElementById('image');
const filePreview = document.getElementById('filePreview');
const chatbotToggle = document.getElementById('chatbotToggle');
const chatbotContainer = document.getElementById('chatbotContainer');
const chatbotClose = document.getElementById('chatbotClose');
const chatInput = document.getElementById('chatInput');
const sendMessage = document.getElementById('sendMessage');
const chatbotMessages = document.getElementById('chatbotMessages');

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    initializeChatbot();
});

function initializeEventListeners() {
    // Form submission
    if (analysisForm) {
        analysisForm.addEventListener('submit', handleFormSubmission);
    }
    
    // File input change
    if (fileInput) {
        fileInput.addEventListener('change', handleFilePreview);
    }
    
    // Chatbot events
    if (chatbotToggle) {
        chatbotToggle.addEventListener('click', toggleChatbot);
    }
    
    if (chatbotClose) {
        chatbotClose.addEventListener('click', closeChatbot);
    }
    
    if (sendMessage) {
        sendMessage.addEventListener('click', sendChatMessage);
    }
    
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
    }
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Form Submission Handler
async function handleFormSubmission(e) {
    e.preventDefault();
    
    const formData = new FormData(analysisForm);
    
    // Validation
    if (!formData.get('image') || formData.get('image').size === 0) {
        showNotification('Please upload an image', 'error');
        return;
    }
    
    if (!formData.get('gender') || !formData.get('occasion')) {
        showNotification('Please fill in all required fields', 'error');
        return;
    }
    
    // Show loading
    analysisForm.style.display = 'none';
    loading.classList.add('show');
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Redirect to results page
            window.location.href = result.redirect;
        } else {
            throw new Error(result.error || 'Analysis failed');
        }
        
    } catch (error) {
        console.error('Analysis error:', error);
        showNotification('Analysis failed. Please try again.', 'error');
        
        // Hide loading and show form
        loading.classList.remove('show');
        analysisForm.style.display = 'block';
    }
}

// File Preview Handler
function handleFilePreview(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            filePreview.innerHTML = `
                <img src="${e.target.result}" alt="Preview" style="max-width: 100px; max-height: 100px; border-radius: 10px;">
                <p style="margin-top: 0.5rem; font-size: 0.9rem; color: #666;">${file.name}</p>
            `;
        };
        reader.readAsDataURL(file);
    }
}

// Chatbot Functions
function initializeChatbot() {
    // Add welcome message if not already present
    const messages = chatbotMessages.querySelectorAll('.message');
    if (messages.length === 0) {
        addBotMessage("Hello! I'm your AI style assistant. Ask me about skincare, outfits, or beauty tips! 💄✨");
    }
}

function toggleChatbot() {
    chatbotContainer.classList.toggle('show');
    if (chatbotContainer.classList.contains('show')) {
        chatInput.focus();
    }
}

function closeChatbot() {
    chatbotContainer.classList.remove('show');
}

async function sendChatMessage() {
    const message = chatInput.value.trim();
    if (!message) return;
    
    // Add user message
    addUserMessage(message);
    chatInput.value = '';
    
    // Show typing indicator
    const typingIndicator = addTypingIndicator();
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        const result = await response.json();
        
        // Remove typing indicator
        typingIndicator.remove();
        
        // Add bot response
        addBotMessage(result.response);
        
    } catch (error) {
        console.error('Chat error:', error);
        typingIndicator.remove();
        addBotMessage("Sorry, I'm having trouble responding right now. Please try again!");
    }
}

function addUserMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'message user-message';
    messageElement.innerHTML = `<div class="message-content">${escapeHtml(message)}</div>`;
    chatbotMessages.appendChild(messageElement);
    scrollToBottom();
}

function addBotMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'message bot-message';
    messageElement.innerHTML = `<div class="message-content">${escapeHtml(message)}</div>`;
    chatbotMessages.appendChild(messageElement);
    scrollToBottom();
}

function addTypingIndicator() {
    const typingElement = document.createElement('div');
    typingElement.className = 'message bot-message typing';
    typingElement.innerHTML = `
        <div class="message-content">
            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    chatbotMessages.appendChild(typingElement);
    scrollToBottom();
    return typingElement;
}

function scrollToBottom() {
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

// Utility Functions
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        background: ${type === 'error' ? '#ff6b6b' : '#667eea'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    // Add to document
    document.body.appendChild(notification);
    
    // Remove after 5 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 5000);
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .notification-content {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .typing-dots {
        display: flex;
        gap: 0.25rem;
    }
    
    .typing-dots span {
        width: 6px;
        height: 6px;
        background: #667eea;
        border-radius: 50%;
        animation: typing 1.4s infinite ease-in-out;
    }
    
    .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
    .typing-dots span:nth-child(2) { animation-delay: -0.16s; }
    
    @keyframes typing {
        0%, 80%, 100% {
            transform: scale(0.8);
            opacity: 0.5;
        }
        40% {
            transform: scale(1);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.feature-card, .result-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        observer.observe(el);
    });
});

// Add fadeInUp animation
const animationStyle = document.createElement('style');
animationStyle.textContent = `
    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(animationStyle);

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (header) {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(255, 255, 255, 0.98)';
            header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.boxShadow = 'none';
        }
    }
});

// Parallax effect for floating shapes
window.addEventListener('scroll', () => {
    const shapes = document.querySelectorAll('.shape');
    const scrolled = window.pageYOffset;
    
    shapes.forEach((shape, index) => {
        const rate = scrolled * (0.5 + index * 0.1);
        shape.style.transform = `translateY(${rate}px)`;
    });
});