# # Copyright 2025 Google LLC
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

import os
from dataclasses import dataclass

# ── Ollama runs locally, no Google Cloud auth needed ──────────────────────────
OLLAMA_BASE_URL = os.environ["OLLAMA_BASE_URL"]  

# Keep these in case other parts of your code still use Google/Vertex
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "False") 


@dataclass
class ResearchConfiguration:
    """Configuration for research-related models and parameters.

    Attributes:
        critic_model (str): Model for evaluation tasks.
        worker_model (str): Model for working/generation tasks.
        max_search_iterations (int): Maximum search iterations allowed.
    """

    # critic_model: str = "gemini-2.5-pro"
    # worker_model: str = "gemini-2.5-flash"
    critic_model: str = "ollama/gemma4:e4b"   
    worker_model: str = "ollama/gemma4:e4b"  

    max_search_iterations: int = 5         # unchanged


config = ResearchConfiguration()

