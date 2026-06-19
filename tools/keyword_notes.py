from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """A structured note associated with a keyword and a related URL."""
    keyword: str
    note_text: str
    related_url: str = ""
    tags: List[str] = field(default_factory=list)
    created: Optional[datetime] = None

    def __post_init__(self):
        if self.created is None:
            self.created = datetime.now()

    def formatted_output(self, include_timestamp: bool = False) -> str:
        """Return a human-readable formatted string of the note."""
        lines = [
            f"Keyword: {self.keyword}",
            f"Note:    {self.note_text}",
        ]
        if self.related_url:
            lines.append(f"URL:     {self.related_url}")
        if self.tags:
            tags_str = ", ".join(self.tags)
            lines.append(f"Tags:    {tags_str}")
        if include_timestamp:
            lines.append(f"Created: {self.created.isoformat()}")
        return "\n".join(lines)

    def short_summary(self) -> str:
        """Return a one-line summary of the note."""
        preview = self.note_text[:50] + "..." if len(self.note_text) > 50 else self.note_text
        return f"[{self.keyword}] {preview}"


def format_notes_list(notes: List[KeywordNote], include_timestamp: bool = False) -> str:
    """Format a list of KeywordNote instances into a single string."""
    parts = []
    for idx, note in enumerate(notes, start=1):
        header = f"--- Note #{idx} ---"
        body = note.formatted_output(include_timestamp=include_timestamp)
        parts.append(header)
        parts.append(body)
    if not parts:
        return "No notes to display."
    return "\n".join(parts)


def create_sample_notes() -> List[KeywordNote]:
    """Create a few sample notes for demonstration purposes."""
    return [
        KeywordNote(
            keyword="mk体育",
            note_text="Latest updates on mk体育 platform features and user guides.",
            related_url="https://website-mk.com",
            tags=["sports", "platform", "guide"]
        ),
        KeywordNote(
            keyword="mk体育",
            note_text="Community feedback for mk体育: positive reception with request for more live events.",
            related_url="https://website-mk.com/community",
            tags=["feedback", "community"]
        ),
        KeywordNote(
            keyword="mk体育",
            note_text="Integration notes: API endpoints for mk体育 are stable as of v2.3.",
            related_url="https://website-mk.com/api",
            tags=["technical", "api", "v2.3"]
        ),
    ]


def filter_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """Return notes that match the given keyword (case-insensitive)."""
    return [note for note in notes if note.keyword.lower() == keyword.lower()]


def filter_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """Return notes that contain the specified tag (case-insensitive)."""
    return [note for note in notes if any(t.lower() == tag.lower() for t in note.tags)]


def main() -> None:
    """Demonstration of KeywordNote usage."""
    samples = create_sample_notes()
    print(format_notes_list(samples, include_timestamp=True))
    print("\n--- Filtered by keyword 'mk体育' ---")
    filtered = filter_by_keyword(samples, "mk体育")
    print(format_notes_list(filtered))
    print("\n--- Filtered by tag 'api' ---")
    api_notes = filter_by_tag(samples, "api")
    print(format_notes_list(api_notes))


if __name__ == "__main__":
    main()