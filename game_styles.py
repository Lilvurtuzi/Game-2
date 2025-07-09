import streamlit as st

def apply_game_styles():
    """Apply vibrant game-like styling to the Streamlit app"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #0f0f23 75%, #1a1a2e 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Neon glow effect */
    .main-header {
        font-family: 'Orbitron', monospace;
        text-align: center;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 2rem;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ff00);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neonGlow 2s ease-in-out infinite alternate, gradientShift 4s ease infinite;
        text-shadow: 0 0 20px #00ffff, 0 0 30px #ff00ff, 0 0 40px #ffff00;
    }
    
    @keyframes neonGlow {
        from { filter: drop-shadow(0 0 20px #00ffff) drop-shadow(0 0 30px #ff00ff); }
        to { filter: drop-shadow(0 0 30px #ff00ff) drop-shadow(0 0 40px #00ffff); }
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
        border-right: 2px solid #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-family: 'Orbitron', monospace;
        font-weight: bold;
        font-size: 1.1rem;
        text-transform: uppercase;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
        transition: all 0.3s ease;
        animation: buttonPulse 2s ease-in-out infinite;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.7);
        background: linear-gradient(45deg, #00ffff, #ff00ff);
    }
    
    @keyframes buttonPulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 0, 255, 0.5); }
        50% { box-shadow: 0 0 30px rgba(0, 255, 255, 0.7); }
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #00ffff;
        border-radius: 15px;
        color: #00ffff;
        font-family: 'Orbitron', monospace;
        padding: 0.75rem;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff00ff;
        box-shadow: 0 0 25px rgba(255, 0, 255, 0.5);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div > select {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ffff00;
        border-radius: 15px;
        color: #ffff00;
        font-family: 'Orbitron', monospace;
        box-shadow: 0 0 15px rgba(255, 255, 0, 0.3);
    }
    
    /* Challenge box styling */
    .challenge-box {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.1), rgba(255, 0, 255, 0.1));
        padding: 2rem;
        border-radius: 20px;
        border: 3px solid;
        border-image: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00) 1;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
        animation: boxGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes boxGlow {
        from { box-shadow: 0 0 30px rgba(0, 255, 255, 0.2); }
        to { box-shadow: 0 0 40px rgba(255, 0, 255, 0.3); }
    }
    
    /* Timer display */
    .timer-display {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px #ff00ff;
        animation: timerPulse 1s ease-in-out infinite;
    }
    
    @keyframes timerPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Score display */
    .score-display {
        font-family: 'Orbitron', monospace;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #00ff00;
        text-shadow: 0 0 20px #00ff00;
        animation: scoreGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes scoreGlow {
        from { text-shadow: 0 0 20px #00ff00; }
        to { text-shadow: 0 0 30px #00ff00, 0 0 40px #00ff00; }
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, rgba(0, 255, 0, 0.1), rgba(0, 255, 255, 0.1));
        padding: 1rem;
        border-radius: 15px;
        border: 2px solid #00ff00;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #ff00ff, #00ffff, #ffff00);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.5);
    }
    
    /* Leaderboard styling */
    .leaderboard-header {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #ffff00, #00ff00);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px #ffff00;
        margin-bottom: 2rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, rgba(255, 0, 255, 0.2), rgba(0, 255, 255, 0.2));
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #00ffff;
        font-family: 'Orbitron', monospace;
        font-weight: bold;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 0, 255, 0.3);
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #00ffff;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background: linear-gradient(135deg, rgba(0, 255, 0, 0.2), rgba(0, 255, 255, 0.2));
        border: 2px solid #00ff00;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255, 0, 0, 0.2), rgba(255, 0, 255, 0.2));
        border: 2px solid #ff0000;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 255, 0, 0.2), rgba(255, 165, 0, 0.2));
        border: 2px solid #ffff00;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(255, 255, 0, 0.3);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #00ffff;
        font-family: 'Orbitron', monospace;
        font-size: 1.2rem;
        margin-top: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.1), rgba(255, 0, 255, 0.1));
        border-radius: 15px;
        border: 2px solid #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def create_confetti_animation():
    """Create confetti animation for high scores"""
    return """
    <script>
    function createConfetti() {
        const colors = ['#ff00ff', '#00ffff', '#ffff00', '#00ff00', '#ff0000'];
        const confettiContainer = document.createElement('div');
        confettiContainer.style.position = 'fixed';
        confettiContainer.style.top = '0';
        confettiContainer.style.left = '0';
        confettiContainer.style.width = '100%';
        confettiContainer.style.height = '100%';
        confettiContainer.style.pointerEvents = 'none';
        confettiContainer.style.zIndex = '9999';
        document.body.appendChild(confettiContainer);
        
        for (let i = 0; i < 100; i++) {
            const confetti = document.createElement('div');
            confetti.style.position = 'absolute';
            confetti.style.width = Math.random() * 10 + 5 + 'px';
            confetti.style.height = confetti.style.width;
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.left = Math.random() * 100 + '%';
            confetti.style.top = '-20px';
            confetti.style.borderRadius = '50%';
            confetti.style.animation = `fall ${Math.random() * 3 + 2}s linear forwards`;
            confetti.style.boxShadow = '0 0 15px ' + confetti.style.backgroundColor;
            confettiContainer.appendChild(confetti);
            
            // Add sparkles
            if (Math.random() > 0.7) {
                const sparkle = document.createElement('div');
                sparkle.style.position = 'absolute';
                sparkle.style.width = '3px';
                sparkle.style.height = '3px';
                sparkle.style.backgroundColor = '#ffffff';
                sparkle.style.left = Math.random() * 100 + '%';
                sparkle.style.top = '-10px';
                sparkle.style.animation = `sparkle ${Math.random() * 2 + 1}s ease-out forwards`;
                sparkle.style.boxShadow = '0 0 10px #ffffff';
                confettiContainer.appendChild(sparkle);
            }
        }
        
        setTimeout(() => {
            document.body.removeChild(confettiContainer);
        }, 5000);
    }
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fall {
            to {
                transform: translateY(100vh) rotate(720deg);
            }
        }
        @keyframes sparkle {
            0% { opacity: 1; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
            100% { opacity: 0; transform: scale(0); }
        }
    `;
    document.head.appendChild(style);
    
    createConfetti();
    </script>
    """

def create_timer_display(time_left):
    """Create animated timer display"""
    color = "#00ff00" if time_left > 15 else "#ffff00" if time_left > 5 else "#ff0000"
    return f"""
    <div style="
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: {color};
        text-shadow: 0 0 30px {color};
        animation: timerPulse 1s ease-in-out infinite;
        margin: 1rem 0;
    ">
        ⏱️ Time Left: {time_left:.1f}s
    </div>
    """

def create_score_display(score, max_score=100):
    """Create animated score display"""
    percentage = (score / max_score) * 100
    color = "#00ff00" if percentage >= 80 else "#ffff00" if percentage >= 60 else "#ff0000"
    
    return f"""
    <div style="
        font-family: 'Orbitron', monospace;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: {color};
        text-shadow: 0 0 20px {color};
        animation: scoreGlow 2s ease-in-out infinite alternate;
        margin: 1rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.5));
        border-radius: 15px;
        border: 2px solid {color};
        box-shadow: 0 0 20px {color}40;
    ">
        🎯 Final Score: {score}/{max_score}
    </div>
    """

def create_background_music():
    """Create background music for the game using simple beep sounds"""
    return """
    <script>
    let isPlaying = false;
    let intervalId;
    
    function createSimpleBeep(frequency, duration, volume = 0.1) {
        return new Promise((resolve) => {
            try {
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.frequency.value = frequency;
                oscillator.type = 'sine';
                
                gainNode.gain.setValueAtTime(volume, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + duration);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + duration);
                
                setTimeout(resolve, duration * 1000);
            } catch (error) {
                console.log('Audio error:', error);
                resolve();
            }
        });
    }
    
    async function playBackgroundTune() {
        if (!isPlaying) return;
        
        const notes = [523, 659, 784, 1047]; // C5, E5, G5, C6
        
        for (let note of notes) {
            if (!isPlaying) break;
            await createSimpleBeep(note, 0.3, 0.05);
            await new Promise(resolve => setTimeout(resolve, 200));
        }
        
        // Wait before repeating
        if (isPlaying) {
            setTimeout(playBackgroundTune, 2000);
        }
    }
    
    function startBackgroundMusic() {
        if (!isPlaying) {
            isPlaying = true;
            console.log('Starting background music');
            playBackgroundTune();
        }
    }
    
    // Start music on user interaction
    document.addEventListener('click', startBackgroundMusic, { once: true });
    document.addEventListener('keydown', startBackgroundMusic, { once: true });
    
    // Alternative: Use HTML5 audio for click sounds
    window.playClickSound = function() {
        createSimpleBeep(800, 0.1, 0.2);
    };
    
    // Add click sound to all buttons
    document.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') {
            window.playClickSound();
        }
    });
    </script>
    """

def create_sound_effect(effect_type):
    """Create sound effects for different game events"""
    if effect_type == "success":
        return """
        <script>
        async function playSuccessSound() {
            try {
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                await audioContext.resume();
                
                const notes = [523, 659, 784, 1047]; // C5, E5, G5, C6
                
                for (let i = 0; i < notes.length; i++) {
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    oscillator.frequency.value = notes[i];
                    oscillator.type = 'triangle';
                    
                    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                    gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.3);
                    
                    oscillator.start(audioContext.currentTime);
                    oscillator.stop(audioContext.currentTime + 0.3);
                    
                    await new Promise(resolve => setTimeout(resolve, 150));
                }
                
                console.log('Success sound played');
            } catch (error) {
                console.log('Audio error:', error);
                // Fallback: Visual feedback
                document.body.style.backgroundColor = '#00ff00';
                setTimeout(() => document.body.style.backgroundColor = '', 200);
            }
        }
        
        playSuccessSound();
        </script>
        """
    elif effect_type == "timer":
        return """
        <script>
        function playTimerSound() {
            try {
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                audioContext.resume();
                
                const oscillator = audioContext.createOscillator();
                const gainNode = audioContext.createGain();
                
                oscillator.connect(gainNode);
                gainNode.connect(audioContext.destination);
                
                oscillator.frequency.value = 1000;
                oscillator.type = 'square';
                
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.2);
                
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.2);
                
                console.log('Timer sound played');
            } catch (error) {
                console.log('Audio error:', error);
                // Fallback: Visual feedback
                document.body.style.backgroundColor = '#ffff00';
                setTimeout(() => document.body.style.backgroundColor = '', 100);
            }
        }
        
        playTimerSound();
        </script>
        """
    elif effect_type == "failure":
        return """
        <script>
        async function playFailureSound() {
            try {
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                await audioContext.resume();
                
                const notes = [440, 392, 349, 294]; // A4, G4, F4, D4 (descending)
                
                for (let i = 0; i < notes.length; i++) {
                    const oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    
                    oscillator.frequency.value = notes[i];
                    oscillator.type = 'sawtooth';
                    
                    gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
                    gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.4);
                    
                    oscillator.start(audioContext.currentTime);
                    oscillator.stop(audioContext.currentTime + 0.4);
                    
                    await new Promise(resolve => setTimeout(resolve, 200));
                }
                
                console.log('Failure sound played');
            } catch (error) {
                console.log('Audio error:', error);
                // Fallback: Visual feedback
                document.body.style.backgroundColor = '#ff0000';
                setTimeout(() => document.body.style.backgroundColor = '', 200);
            }
        }
        
        playFailureSound();
        </script>
        """
    else:
        return ""

def create_floating_particles():
    """Create floating particles animation for background"""
    return """
    <script>
    function createFloatingParticles() {
        const particleContainer = document.createElement('div');
        particleContainer.style.position = 'fixed';
        particleContainer.style.top = '0';
        particleContainer.style.left = '0';
        particleContainer.style.width = '100%';
        particleContainer.style.height = '100%';
        particleContainer.style.pointerEvents = 'none';
        particleContainer.style.zIndex = '1';
        document.body.appendChild(particleContainer);
        
        const colors = ['#ff00ff', '#00ffff', '#ffff00', '#00ff00'];
        
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.style.position = 'absolute';
            particle.style.width = '4px';
            particle.style.height = '4px';
            particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            particle.style.borderRadius = '50%';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animation = `float ${Math.random() * 10 + 5}s ease-in-out infinite`;
            particle.style.boxShadow = `0 0 10px ${particle.style.backgroundColor}`;
            particleContainer.appendChild(particle);
        }
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes float {
                0%, 100% { transform: translateY(0px) translateX(0px); }
                25% { transform: translateY(-20px) translateX(10px); }
                50% { transform: translateY(0px) translateX(-10px); }
                75% { transform: translateY(20px) translateX(5px); }
            }
        `;
        document.head.appendChild(style);
    }
    
    createFloatingParticles();
    </script>
    """

def create_pulse_animation():
    """Create pulsing animation for important elements"""
    return """
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s ease-in-out infinite;
    }
    </style>
    """