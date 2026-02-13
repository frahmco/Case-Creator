from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
from typing import Iterable

class Hasher:

    def __init__(self, algorithm: str = "md5", workers: int = 4):

        supported = hashlib.algorithms_guaranteed
        algo = algorithm.lower()
        print(f"Hash algo selected: {algo}")
        if algo not in supported:
            raise ValueError(f"Unsupported hash algorithm: {algo}")
        self.algorithm = algo
        self.workers = workers

        self.algorithm = algorithm
        self.workers = workers
    
    def get_workers(self) -> int:
        return self.workers
    
    def set_workers(self, count: int) -> None:
        if count < 1:
            raise ValueError("Worker count must be at least 1.")
        self.workers = count
    
    def _hash_file(self, file: Path) -> str:
        hash = hashlib.new(self.algorithm)

        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash.update(chunk)
        return hash.hexdigest()
    
    def hash_files(self, files: Iterable[str | Path]) -> dict[Path, str]:
    
        paths = [Path(f).resolve() for f in files]

        for p in paths:
            if not p.is_file():
                raise ValueError(f"Invalid file: {p}")

        results: dict[Path, str] = {}

        def task(path: Path):
            return path, self._hash_file(path)

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            for path, digest in executor.map(task, paths):
                results[path] = digest

        return results