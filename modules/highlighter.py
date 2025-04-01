from typing import List, Tuple
import re

class Highlighter:
    def highlight(self, text: str, edits: List[Tuple[str, str, int, int, str, int, int]]) -> str:
        highlighted_text = text
        for edit in edits:
            error_type, original_text, start, end, corrected_text, _, _ = edit
            highlighted_text = highlighted_text.replace(
                original_text,
                f"<c type='{error_type}' edit='{corrected_text}'>{original_text}</c>"
            )
        return highlighted_text
