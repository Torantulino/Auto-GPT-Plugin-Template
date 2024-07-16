import requests
from typing import Any, Dict, List, Optional, Tuple
from .. import AutoGPTPluginTemplate

class MaterialsProjectPlugin(AutoGPTPluginTemplate):
    def __init__(self):
        super().__init__()
        self._name = "MaterialsProjectPlugin"
        self._version = "0.1.0"
        self._description = "A plugin to make API requests to the Materials Project API."
        self.api_key = "vYixarnBRye6p1l9eCIZk6XIRNHY4spO"
        self.base_url = "https://next-gen.materialsproject.org/api/v2/"

    def can_handle_on_response(self) -> bool:
        return True

    def on_response(self, response: str, *args, **kwargs) -> str:
        endpoint = "materials"
        params = {"search": response}
        headers = {"X-API-KEY": self.api_key}
        
        api_response = requests.get(f"{self.base_url}{endpoint}", headers=headers, params=params)
        return api_response.json()

    def can_handle_post_prompt(self) -> bool:
        return False

    def post_prompt(self, prompt: Any) -> Any:
        pass

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(self, prompt: Any, messages: List[Dict[str, str]]) -> Optional[str]:
        pass

    def can_handle_post_planning(self) -> bool:
        return False

    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        return False

    def pre_instruction(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        pass

    def can_handle_on_instruction(self) -> bool:
        return False

    def on_instruction(self, messages: List[Dict[str, str]]) -> Optional[str]:
        pass

    def can_handle_post_instruction(self) -> bool:
        return False

    def post_instruction(self, response: str) -> str:
        pass

    def can_handle_pre_command(self) -> bool:
        return False

    def pre_command(self, command_name: str, arguments: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        pass

    def can_handle_post_command(self) -> bool:
        return False

    def post_command(self, command_name: str, response: str) -> str:
        pass

    def can_handle_chat_completion(self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int) -> bool:
        return False

    def handle_chat_completion(self, messages: List[Dict[str, str]], model: str, temperature: float, max_tokens: int) -> str:
        pass

    def can_handle_text_embedding(self, text: str) -> bool:
        return False
    
    def handle_text_embedding(self, text: str) -> list:
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        return False

    def user_input(self, user_input: str) -> str:
        pass

    def can_handle_report(self) -> bool:
        return False

    def report(self, message: str) -> None:
        pass
