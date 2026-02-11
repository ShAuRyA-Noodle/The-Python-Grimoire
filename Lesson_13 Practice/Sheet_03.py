"""
Minimal Flask Application

Description
-----------
This module defines a basic Flask web server with a single root endpoint.
It demonstrates routing, application initialization, and safe execution
using the __main__ guard.
"""

from flask import Flask

# Application factory (recommended structure even for small apps)
def create_app() -> Flask:
    """
    Create and configure the Flask application instance.

    Returns:
        Flask: Configured Flask app.
    """
    app = Flask(__name__)

    @app.route("/")
    def hello_world() -> str:
        """Return a simple greeting message."""
        return "<p>Hello, World!</p>"

    return app


def main() -> None:
    """
    Application entry point.

    Starts the Flask development server when the script
    is executed directly.
    """
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
