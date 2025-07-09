# 🎮 Rational Function Rumble

A vibrant, gamified educational app for teaching precalculus students to graph rational functions through timed challenges and leaderboards.

## Features

- **Interactive Gameplay**: 30-second timed challenges with real-time feedback
- **Difficulty Levels**: Easy, Medium, and Hard modes with progressively complex functions
- **Visual Learning**: Interactive graphs with highlighted features (asymptotes, holes, intercepts)
- **Gamification**: Scoring system, leaderboards, and progress tracking
- **Neon Gaming Aesthetic**: Vibrant colors, animations, and visual effects
- **Audio Feedback**: Background music and sound effects (browser-dependent)

## Mathematical Concepts Covered

- X-intercepts and Y-intercepts
- Vertical asymptotes
- Holes (removable discontinuities)
- End behavior analysis
- Rational function graphing

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/rational-function-rumble.git
cd rational-function-rumble
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter your name in the sidebar
2. Select a difficulty level
3. Click "Start New Challenge" to begin
4. Analyze the displayed rational function
5. Enter your answers for:
   - X-intercepts (comma-separated)
   - Y-intercept
   - Vertical asymptotes (comma-separated)
   - Holes (x,y coordinates if present)
6. Submit before the 30-second timer runs out
7. View your score and detailed feedback
8. Save your score to the leaderboard

## Project Structure

```
rational-function-rumble/
├── app.py              # Main Streamlit application
├── utils.py            # Mathematical utilities and function generation
├── leaderboard.py      # Leaderboard data management
├── game_styles.py      # Custom CSS styling and animations
├── leaderboard.csv     # Persistent score data
├── requirements.txt    # Python dependencies
└── .streamlit/
    └── config.toml     # Streamlit configuration
```

## Technical Details

- **Framework**: Streamlit for web interface
- **Mathematics**: SymPy for symbolic computation
- **Visualization**: Matplotlib for function graphing
- **Data Storage**: CSV-based leaderboard system
- **Styling**: Custom CSS with neon themes and animations

## Scoring System

- X-intercepts: 25 points
- Y-intercept: 20 points
- Vertical asymptotes: 30 points
- Holes: 25 points
- Maximum score: 100 points

## Browser Compatibility

- Modern browsers with JavaScript enabled
- Audio features require Web Audio API support
- Visual feedback provided when audio is unavailable

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Educational Use

This app is designed for:
- Precalculus students learning rational functions
- Mathematics teachers looking for interactive tools
- Anyone wanting to practice graphing rational functions

## Support

If you encounter issues or have suggestions, please create an issue in the GitHub repository.