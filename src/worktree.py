from pathlib import Path
from typing import Optional

from repository_path import RepositoryPath

class Worktree:
    def __init__(self, repository_path: RepositoryPath):
        self.repo_path = repository_path

    @property
    def root_dir(self) -> Path:
        repo_dir = self.repo_path.get_repo_dir()
        if repo_dir is None:
            raise ValueError("Repository directory not found")
        return repo_dir.parent

    def find_paths(self, file_path: str, start_dir: Optional[Path] = None) -> list[Path]:
        start_dir = start_dir or Path.cwd()
        result_paths: list[Path] = []
        
        if file_path in (".", "./"):
            result_paths = [p for p in start_dir.rglob("*") if p.is_file()]
        elif file_path in ("..", "../"):
            parent_dir = start_dir.parent
            result_paths = [p for p in parent_dir.rglob("*") if p.is_file()]
        else:
            # TODO: write test code for glob pattern
            if any(char in file_path for char in ["*", "?", "[", "]"]):
                result_paths = [p for p in start_dir.rglob(file_path) if p.is_file()]
            else:
                candidate = start_dir / file_path
                if candidate.exists():
                    if candidate.is_file():
                        result_paths = [candidate]
                    elif candidate.is_dir():
                        result_paths = [p for p in candidate.rglob("*") if p.is_file()]
        return result_paths
    
    