# GitHub Export Guide

## Files Ready for Export

Your Rational Function Rumble project is now ready for GitHub! Here are the key files:

### Essential Files
- `README.md` - Complete project documentation
- `LICENSE` - MIT license for open source sharing
- `.gitignore` - Prevents unnecessary files from being tracked
- `requirements_github.txt` - Python dependencies for GitHub users
- `.streamlit/config.toml` - Streamlit configuration

### Project Files
- `app.py` - Main application
- `utils.py` - Mathematical utilities
- `leaderboard.py` - Score tracking system
- `game_styles.py` - Visual styling and animations
- `leaderboard.csv` - Sample leaderboard data

## How to Export to GitHub

### Method 1: Using GitHub Desktop (Easiest)
1. Download and install GitHub Desktop
2. Create a new repository on GitHub.com
3. Clone it to your computer
4. Copy all project files to the cloned folder
5. Commit and push changes

### Method 2: Using Command Line
1. Create a new repository on GitHub.com (don't initialize with README)
2. Copy the repository URL
3. In your project folder, run:
```bash
git init
git add .
git commit -m "Initial commit - Rational Function Rumble game"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

### Method 3: Using Git ZIP Upload
1. Create a new repository on GitHub.com
2. Download your project as a ZIP file
3. Extract and upload files directly through GitHub's web interface

## Important Notes

### Dependencies
- Users will need to run `pip install -r requirements_github.txt` after cloning
- The app runs with `streamlit run app.py`

### File Structure
Make sure these files are in the root directory:
```
your-repo/
├── app.py
├── utils.py
├── leaderboard.py
├── game_styles.py
├── README.md
├── LICENSE
├── .gitignore
├── requirements_github.txt
├── leaderboard.csv
└── .streamlit/
    └── config.toml
```

### Repository Settings
- Choose a descriptive name like `rational-function-rumble`
- Make it public for educational use
- Add topics: `streamlit`, `education`, `mathematics`, `precalculus`, `game`

## After Export

1. Update the README.md with your actual GitHub username/repo name
2. Consider adding screenshots to showcase the game
3. Test the installation instructions on a fresh environment
4. Share with educators and students!

## Troubleshooting

If users report issues:
- Check that all files are present
- Verify Python version compatibility (3.8+)
- Ensure all dependencies install correctly
- Test the Streamlit app locally before sharing

Your project is now ready to share with the world! 🚀