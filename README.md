# ParkNTrailTracker
ParkNTrailTracker lets users explore and track national parks and park trails they have visited. Helpful for deciding your next national park to visit or to remember your best hiking memories, this tracker has your back.

## Setup and Running

### Using uv
1. 'curl -LsSf https://astral.sh/uv/install.sh | sh' (for macOS/Linux)
    OR 'pip install uv' if you have pip installed
2. Clone the repo: 'git clone [<your-repo-url>](https://github.com/chanel-koh/park-n-trail-tracker.git)'
3. 'cd park-n-trail-tracker'
4. To create and sync the environment: 'uv sync'
5. Running the project: 'uv run python main.py'

### Setup Kaggle API for seeding database
1. Go to Kaggle -> Settings -> API
2. Create a new API token
3. In your terminal: 'KAGGLE_API_TOKEN=your_token_here'
