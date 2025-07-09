import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sympy.abc import x
from utils import generate_function, get_features, graph_function
from leaderboard import load_leaderboard, save_leaderboard
from game_styles import apply_game_styles, create_confetti_animation, create_timer_display, create_score_display, create_background_music, create_sound_effect, create_floating_particles, create_pulse_animation

# Page configuration
st.set_page_config(
    page_title="Rational Function Rumble",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply neon game styling and initialize animations
apply_game_styles()
st.markdown(create_pulse_animation(), unsafe_allow_html=True)
st.markdown(create_floating_particles(), unsafe_allow_html=True)

# Add audio initialization with user interaction prompt
st.markdown("""
<div style="text-align: center; margin: 10px 0; padding: 10px; background: linear-gradient(45deg, rgba(255,0,255,0.1), rgba(0,255,255,0.1)); border-radius: 10px; border: 1px solid #00ffff;">
    <small style="color: #00ffff;">🔊 Audio may not work in all browsers. Visual feedback will show if sound is unavailable.</small>
</div>
""", unsafe_allow_html=True)

st.markdown(create_background_music(), unsafe_allow_html=True)

# Initialize session state
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'current_function' not in st.session_state:
    st.session_state.current_function = None
if 'current_features' not in st.session_state:
    st.session_state.current_features = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'games_played' not in st.session_state:
    st.session_state.games_played = 0
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

# Main title
st.markdown('<h1 class="main-header">🎮 Rational Function Rumble 🎮</h1>', unsafe_allow_html=True)

# Sidebar for game controls
with st.sidebar:
    st.header("🎯 Game Controls")
    
    # Player name input
    player_name = st.text_input("🏷️ Enter your name:", placeholder="Player Name")
    
    # Difficulty selection
    difficulty = st.selectbox(
        "🎲 Choose difficulty:",
        ["Easy", "Medium", "Hard"],
        help="Easy: Simple linear factors\nMedium: Quadratic factors\nHard: Complex rational functions"
    )
    
    # Audio test button
    if st.button("🎵 Test Audio", help="Click to test sound effects"):
        st.markdown(create_sound_effect("success"), unsafe_allow_html=True)
        st.success("Audio test played!")
    
    # Difficulty description
    if difficulty == "Easy":
        st.info("🟢 **Easy Mode**: Simple rational functions with linear factors")
    elif difficulty == "Medium":
        st.info("🟡 **Medium Mode**: Rational functions with quadratic factors")
    else:
        st.info("🔴 **Hard Mode**: Complex rational functions with multiple factors")
    
    # Game statistics
    st.subheader("📊 Your Stats")
    st.metric("🎮 Games Played", st.session_state.games_played)
    st.metric("💯 Total Score", st.session_state.total_score)
    if st.session_state.games_played > 0:
        avg_score = st.session_state.total_score / st.session_state.games_played
        st.metric("📈 Average Score", f"{avg_score:.1f}")

# Main game area
if not player_name:
    st.warning("🚨 Please enter your name to start playing!")
    st.stop()

# Start new game button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start New Challenge", type="primary", use_container_width=True, key="start_button"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()
        st.session_state.current_function = generate_function(difficulty)
        st.session_state.current_features = get_features(st.session_state.current_function)
        st.session_state.score = 0
        st.rerun()

# Game logic
if st.session_state.game_started and st.session_state.current_function is not None:
    # Timer calculation
    elapsed_time = time.time() - st.session_state.start_time
    time_left = max(0, 30 - elapsed_time)
    
    # Timer display with neon effects
    timer_col1, timer_col2, timer_col3 = st.columns([1, 1, 1])
    with timer_col2:
        if time_left > 0:
            st.markdown(create_timer_display(time_left), unsafe_allow_html=True)
            # Add timer sound effect when time is running low
            if time_left <= 5 and time_left > 4:
                st.markdown(create_sound_effect("timer"), unsafe_allow_html=True)
        else:
            st.markdown('<div class="timer-display">⏰ Time\'s Up!</div>', unsafe_allow_html=True)
    
    # Progress bar
    progress = (30 - time_left) / 30
    st.progress(progress)
    
    # Function display and graph
    st.markdown('<div class="challenge-box">', unsafe_allow_html=True)
    st.subheader("🎯 Challenge Function")
    
    # Display the function in LaTeX format
    latex_expr = sp.latex(st.session_state.current_function)
    st.latex(f"f(x) = {latex_expr}")
    
    # Graph the function
    graph_function(st.session_state.current_function)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Answer form
    if time_left > 0:
        st.subheader("📝 Your Answers")
        
        with st.form("answer_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                x_intercepts = st.text_input(
                    "🎯 X-intercepts (comma-separated):",
                    placeholder="e.g., -2, 1, 3",
                    help="Enter the x-values where the function crosses the x-axis"
                )
                
                holes = st.text_input(
                    "🕳️ Holes (x,y coordinates):",
                    placeholder="e.g., -1,2 or leave empty",
                    help="Enter hole coordinates if any exist"
                )
            
            with col2:
                y_intercept = st.text_input(
                    "🎯 Y-intercept:",
                    placeholder="e.g., 0.5",
                    help="Enter the y-value where the function crosses the y-axis"
                )
                
                asymptotes = st.text_input(
                    "📏 Vertical Asymptotes (comma-separated):",
                    placeholder="e.g., -2, 3",
                    help="Enter the x-values of vertical asymptotes"
                )
            
            submitted = st.form_submit_button("🚀 Submit Answers", type="primary", use_container_width=True)
    else:
        submitted = False
    
    # Scoring and results
    if submitted or time_left <= 0:
        st.session_state.game_started = False
        
        if time_left <= 0:
            st.error("⏰ Time's up! You scored 0 points.")
            st.markdown(create_sound_effect("failure"), unsafe_allow_html=True)
            final_score = 0
        else:
            # Calculate score
            def parse_numbers(text):
                try:
                    if not text.strip():
                        return []
                    return sorted([float(x.strip()) for x in text.split(",") if x.strip()])
                except:
                    return []
            
            def parse_hole(text):
                try:
                    if not text.strip():
                        return None
                    parts = text.split(",")
                    return (float(parts[0].strip()), float(parts[1].strip()))
                except:
                    return None
            
            user_x_intercepts = parse_numbers(x_intercepts)
            user_y_intercept = y_intercept.strip()
            user_holes = parse_hole(holes)
            user_asymptotes = parse_numbers(asymptotes)
            
            actual = st.session_state.current_features
            score = 0
            feedback = []
            
            # Check X-intercepts (25 points)
            if user_x_intercepts:
                actual_x = [round(float(x), 2) for x in actual["x_intercepts"]]
                user_x_rounded = [round(x, 2) for x in user_x_intercepts]
                if set(user_x_rounded) == set(actual_x):
                    score += 25
                    feedback.append("✅ X-intercepts: Correct! (+25 points)")
                else:
                    feedback.append(f"❌ X-intercepts: Incorrect. Expected: {actual_x}")
            else:
                feedback.append("❌ X-intercepts: No answer provided")
            
            # Check Y-intercept (20 points)
            if user_y_intercept:
                try:
                    user_y = float(user_y_intercept)
                    if abs(user_y - float(actual["y_intercept"])) < 0.1:
                        score += 20
                        feedback.append("✅ Y-intercept: Correct! (+20 points)")
                    else:
                        feedback.append(f"❌ Y-intercept: Incorrect. Expected: {float(actual['y_intercept']):.2f}")
                except:
                    feedback.append("❌ Y-intercept: Invalid format")
            else:
                feedback.append("❌ Y-intercept: No answer provided")
            
            # Check Vertical Asymptotes (30 points)
            if user_asymptotes:
                actual_asym = [round(float(a), 2) for a in actual["asymptotes"]]
                user_asym_rounded = [round(a, 2) for a in user_asymptotes]
                if set(user_asym_rounded) == set(actual_asym):
                    score += 30
                    feedback.append("✅ Vertical Asymptotes: Correct! (+30 points)")
                else:
                    feedback.append(f"❌ Vertical Asymptotes: Incorrect. Expected: {actual_asym}")
            else:
                feedback.append("❌ Vertical Asymptotes: No answer provided")
            
            # Check Holes (25 points)
            if actual["holes"]:
                if user_holes:
                    actual_hole = actual["holes"][0]  # Assume one hole for simplicity
                    if (abs(user_holes[0] - actual_hole[0]) < 0.1 and 
                        abs(user_holes[1] - actual_hole[1]) < 0.1):
                        score += 25
                        feedback.append("✅ Holes: Correct! (+25 points)")
                    else:
                        feedback.append(f"❌ Holes: Incorrect. Expected: {actual_hole}")
                else:
                    feedback.append("❌ Holes: Missing hole identification")
            else:
                if not user_holes:
                    score += 25
                    feedback.append("✅ Holes: Correct - No holes! (+25 points)")
                else:
                    feedback.append("❌ Holes: No holes exist in this function")
            
            final_score = score
            
            # Display results
            st.subheader("📊 Results")
            
            # Score display with neon effects
            st.markdown(create_score_display(final_score), unsafe_allow_html=True)
            
            if final_score >= 80:
                st.success(f"🎉 Outstanding! You scored {final_score}/100 points!")
                st.markdown(create_confetti_animation(), unsafe_allow_html=True)
                st.markdown(create_sound_effect("success"), unsafe_allow_html=True)
            elif final_score >= 60:
                st.info(f"👍 Good job! You scored {final_score}/100 points!")
                st.markdown(create_sound_effect("success"), unsafe_allow_html=True)
            else:
                st.warning(f"💪 Keep practicing! You scored {final_score}/100 points!")
                st.markdown(create_sound_effect("failure"), unsafe_allow_html=True)
            
            # Detailed feedback
            st.subheader("📝 Detailed Feedback")
            for fb in feedback:
                st.write(fb)
            
            # Show correct answers
            with st.expander("🔍 View Correct Answers"):
                st.write(f"**X-intercepts:** {[round(float(x), 2) for x in actual['x_intercepts']]}")
                st.write(f"**Y-intercept:** {float(actual['y_intercept']):.2f}")
                st.write(f"**Vertical Asymptotes:** {[round(float(a), 2) for a in actual['asymptotes']]}")
                st.write(f"**Holes:** {actual['holes'] if actual['holes'] else 'None'}")
                st.write(f"**End Behavior:** {actual['end_behavior']}")
        
        # Update session statistics
        st.session_state.games_played += 1
        st.session_state.total_score += final_score
        
        # Save to leaderboard
        if st.button("💾 Save Score to Leaderboard", type="primary"):
            df = load_leaderboard()
            new_row = pd.DataFrame({
                'Name': [player_name],
                'Score': [final_score],
                'Difficulty': [difficulty],
                'Date': [pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')]
            })
            df = pd.concat([df, new_row], ignore_index=True)
            save_leaderboard(df)
            st.success("🎯 Score saved to leaderboard!")
            st.rerun()

# Leaderboard section with neon styling
st.markdown('<div class="leaderboard-header">🏆 Leaderboard 🏆</div>', unsafe_allow_html=True)
df = load_leaderboard()

if not df.empty:
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["🥇 Top Scores", "📊 By Difficulty", "📈 Recent Games"])
    
    with tab1:
        top_scores = df.nlargest(10, 'Score')
        
        # Create a more visual leaderboard
        for i, (_, row) in enumerate(top_scores.iterrows()):
            col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
            
            with col1:
                if i == 0:
                    st.markdown("🥇")
                elif i == 1:
                    st.markdown("🥈")
                elif i == 2:
                    st.markdown("🥉")
                else:
                    st.markdown(f"#{i+1}")
            
            with col2:
                st.markdown(f"**{row['Name']}**")
            
            with col3:
                st.markdown(f"**{row['Score']}** pts")
            
            with col4:
                difficulty_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
                st.markdown(f"{difficulty_emoji.get(row['Difficulty'], '⚪')} {row['Difficulty']}")
    
    with tab2:
        for diff in ["Easy", "Medium", "Hard"]:
            diff_data = df[df['Difficulty'] == diff]
            if not diff_data.empty:
                st.subheader(f"{diff} Mode")
                st.dataframe(
                    diff_data.nlargest(5, 'Score')[['Name', 'Score', 'Date']],
                    use_container_width=True
                )
    
    with tab3:
        recent_games = df.nlargest(10, 'Date')
        st.dataframe(recent_games, use_container_width=True)

else:
    st.info("🎮 No scores yet! Be the first to play and make it to the leaderboard!")

# Footer with neon styling
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        🎮 Rational Function Rumble | Learn • Play • Master 🎮
    </div>
    """,
    unsafe_allow_html=True
)
