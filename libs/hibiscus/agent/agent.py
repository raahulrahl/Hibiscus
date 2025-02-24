from __future__ import annotations

from collections import ChainMap, defaultdict, deque
from dataclasses import asdict, dataclass
from os import getenv
from textwrap import dedent
from typing import (
    Any,
    AsyncIterator,
    Callable,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
    cast,
    overload,
)
from uuid import uuid4

from pydantic import BaseModel

from hibiscus.models.base import Model

@dataclass(init=False)
class Agent:
    agent_id: Optional[str] = None
    name: Optional[str] = None
    model: Optional[Model] = None
    description: Optional[str] = None
    introduction: Optional[str] = None

    context: Optional[Dict[str, Any]] = None
    add_context: bool = False
    resolve_context: bool = True

    memory: Optional[Memory] = None

    storage: Optional[AgentStorage] = None
    extra_data: Optional[Dict[str, Any]] = None

    reasoning: bool = False
    reasoning_model: Optional[Model] = None
    reasoning_agent: Optional[Agent] = None
    reasoning_min_steps: int = 1
    reasoning_max_steps: int = 10

    team: Optional[List[Agent]] = None
    team_data: Optional[Dict[str, Any]] = None
    role: Optional[str] = None

    organisation: Optional[Agent] = None
    organisation_data: Optional[Dict[str, Any]] = None

    debug_mode: bool = False
    monitoring: bool = False
    telemetry: bool = True





    