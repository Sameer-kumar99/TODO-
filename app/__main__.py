"""
Entry point for running the Flask app as a module.
Run with: python -m app
"""
from app.app import app

if __name__ == "__main__":
    app.run(debug=True)

