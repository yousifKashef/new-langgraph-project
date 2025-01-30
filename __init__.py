"""React Agent.

This module defines a custom reasoning and action agent graph.
It invokes tools in a simple loop.
"""

from react_agent.graph import graph
import os
__all__ = ["graph"]
os.environ["OPENAI_API_KEY"] = "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"
os.environ["TAVILY_API_KEY"] = "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"
