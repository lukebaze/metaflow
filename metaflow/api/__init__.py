"""
Metaflow API Package

This package provides language-agnostic HTTP API endpoints for Metaflow operations.
It enables external systems to interact with Metaflow flows, runs, and artifacts
through RESTful interfaces.

Main Components:
    - APIServer: The main HTTP server that handles API requests
    - routes: URL routing configuration for API endpoints
    - client: HTTP client for interacting with the API
"""

from .server import APIServer
from .routes import register_routes
from .client import APIClient

__all__ = ["APIServer", "register_routes", "APIClient"]
