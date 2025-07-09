import pandas as pd
import os
import streamlit as st
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.csv"

def load_leaderboard():
    """Load leaderboard from CSV file"""
    try:
        if os.path.exists(LEADERBOARD_FILE):
            df = pd.read_csv(LEADERBOARD_FILE)
            # Ensure all required columns exist
            required_columns = ['Name', 'Score', 'Difficulty', 'Date']
            for col in required_columns:
                if col not in df.columns:
                    if col == 'Difficulty':
                        df[col] = 'Easy'  # Default difficulty
                    elif col == 'Date':
                        df[col] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    else:
                        df[col] = 0 if col == 'Score' else 'Unknown'
            return df
        else:
            # Create empty dataframe with required columns
            return pd.DataFrame(columns=['Name', 'Score', 'Difficulty', 'Date'])
    except Exception as e:
        st.error(f"Error loading leaderboard: {str(e)}")
        return pd.DataFrame(columns=['Name', 'Score', 'Difficulty', 'Date'])

def save_leaderboard(df):
    """Save leaderboard to CSV file"""
    try:
        # Ensure the dataframe has the correct structure
        if 'Name' not in df.columns:
            df['Name'] = 'Unknown'
        if 'Score' not in df.columns:
            df['Score'] = 0
        if 'Difficulty' not in df.columns:
            df['Difficulty'] = 'Easy'
        if 'Date' not in df.columns:
            df['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        # Sort by score (descending) and save
        df_sorted = df.sort_values(by='Score', ascending=False)
        df_sorted.to_csv(LEADERBOARD_FILE, index=False)
        
    except Exception as e:
        st.error(f"Error saving leaderboard: {str(e)}")

def get_top_players(limit=10):
    """Get top players from leaderboard"""
    df = load_leaderboard()
    if df.empty:
        return df
    
    return df.nlargest(limit, 'Score')

def get_player_stats(player_name):
    """Get statistics for a specific player"""
    df = load_leaderboard()
    if df.empty:
        return None
    
    player_games = df[df['Name'] == player_name]
    if player_games.empty:
        return None
    
    return {
        'total_games': len(player_games),
        'best_score': player_games['Score'].max(),
        'average_score': player_games['Score'].mean(),
        'total_score': player_games['Score'].sum(),
        'recent_games': player_games.tail(5)
    }

def add_score(player_name, score, difficulty):
    """Add a new score to the leaderboard"""
    df = load_leaderboard()
    
    new_row = {
        'Name': player_name,
        'Score': score,
        'Difficulty': difficulty,
        'Date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    
    # Add new row to dataframe
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Save updated leaderboard
    save_leaderboard(df)
    
    return df

def clear_leaderboard():
    """Clear all scores from leaderboard (admin function)"""
    try:
        empty_df = pd.DataFrame(columns=['Name', 'Score', 'Difficulty', 'Date'])
        save_leaderboard(empty_df)
        return True
    except Exception as e:
        st.error(f"Error clearing leaderboard: {str(e)}")
        return False
