from scripts.logging_config import logger
from app import schemas
from .problem_fetcher import get_problem_details

def get_extension(language):
    extension_map = {
        "python3": "py",
        "python": "py",
        "pandas": "py",
        "java": "java",
        "c": "c",
        "cpp": "cpp",
        "csharp": "cs",
        "javascript": "js",
        "typescript": "ts",
        "ruby": "rb",
        "swift": "swift",
        "go": "go",
        "kotlin": "kt",
        "scala": "scala",
        "rust": "rs",
        "php": "php",
        "mysql": "sql",
        "bash": "sh",
        "perl": "pl",
        "haskell": "hs",
        "dart": "dart",
        "racket": "rkt",
        "elixir": "ex",
        "erlang": "erl",
        "objective-c": "m",
        "matlab": "m",
        "fsharp": "fs",
        "lua": "lua",
        "groovy": "groovy",
        "vb.net": "vb",
        "fortran": "f90",
        "pascal": "pas",
        "julia": "jl",  # Newly added languages
        "prolog": "pl",
        "scheme": "scm",
        "cobol": "cbl",
        "solidity": "sol",
    }

    return extension_map.get(language.lower(), "txt")  # Default to txt if language not found


def organize_leetcode_solutions(raw_solutions: dict)->schemas.Uploads:
    logger.info("Organizing Leetcode solutions ...")
    
    submissions_dump = raw_solutions["submissions_dump"]
    uploads = []
    for submission in submissions_dump:
        if submission["status_display"] == "Accepted":
            title_slug = submission["title_slug"]
            problemDetails : schemas.ProblemDetails = get_problem_details(title_slug=title_slug)
            code_extension : str = get_extension(submission["lang_name"])
            code : str = submission["code"]
            solution : schemas.Solution = schemas.Solution(code=code,code_extension=code_extension)
            upload : schemas.Upload = schemas.Upload(question=problemDetails,solution=solution)
            uploads.append(upload)
    uploads : schemas.Uploads = schemas.Uploads(uploads=uploads)
    return uploads
            