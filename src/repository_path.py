import os
from typing import Optional
from pathlib import Path

from util.constant import GITOY_DB_FILE, GITOY_DIR


class RepositoryPath:

    def __init__(self, cwd: Optional[Path] = None):
        self.cwd = cwd or Path(os.getcwd())
        self.repo_dir = self.get_repo_dir()

    def get_repo_dir(self, cwd: Optional[Path] = None) -> Optional[Path]:
        current_path = cwd or self.cwd
        while True:
            repo_dir = current_path / GITOY_DIR
            if repo_dir.exists() and repo_dir.is_dir():
                return repo_dir
            if current_path.parent == current_path:
                # Reached the root directory
                return None
            current_path = current_path.parent

    def get_repo_db_path(self) -> Optional[Path]:
        repo_dir = self.get_repo_dir()
        if repo_dir is None:
            return None
        return Path(repo_dir, GITOY_DB_FILE)

    def create_repo_dir(self):
        if self.repo_dir is not None:
            return self.repo_dir
        
        self.repo_dir = self.cwd / GITOY_DIR
        self.repo_dir.mkdir(parents=True, exist_ok=True)
        return self.repo_dir
    
    def create_repo_db_path(self):
        return Path(self.cwd, GITOY_DIR, GITOY_DB_FILE)