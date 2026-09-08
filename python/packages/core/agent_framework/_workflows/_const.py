# Copyright (c) Microsoft. All rights reserved.

from dataclasses import dataclass
from typing import Any

# Default maximum iterations for workflow execution.
DEFAULT_MAX_ITERATIONS = 100

# Key used to store executor state in state.
EXECUTOR_STATE_KEY = "_executor_state"

# Key used to store edge runner delivery state (for example, fan-in buffers) in state.
EDGE_STATE_KEY = "_edge_state"

# Source identifier for internal workflow messages.
INTERNAL_SOURCE_PREFIX = "internal"

# State key for storing run kwargs that should be passed to agent invocations.
# Used by all orchestration patterns (Sequential, Concurrent, GroupChat, Handoff, Magentic)
# to pass kwargs from workflow.run() through to agent.run() and @tool functions.
WORKFLOW_RUN_KWARGS_KEY = "_workflow_run_kwargs"

# State keys used to preserve caller-provided kwargs for nested workflow routing.
RAW_FUNCTION_INVOCATION_KWARGS_KEY = "_raw_function_invocation_kwargs"
RAW_CLIENT_KWARGS_KEY = "_raw_client_kwargs"


@dataclass(frozen=True)
class ResolvedWorkflowInvocationKwargs:
    """Internal separation of global and executor-specific invocation kwargs."""

    global_kwargs: dict[str, Any] | None = None
    executor_kwargs: dict[str, Any] | None = None


def INTERNAL_SOURCE_ID(executor_id: str) -> str:
    """Generate an internal source ID for a given executor."""
    return f"{INTERNAL_SOURCE_PREFIX}:{executor_id}"
