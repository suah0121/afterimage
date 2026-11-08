import json
import uuid
from pathlib import Path
from datetime import datetime

# 프로젝트 루트 경로
BASE_DIR = Path(__file__).resolve().parent.parent

# 데이터 파일 경로
PROJECTS_FILE = BASE_DIR / "afterimage_projects.json"
EXHIBITIONS_FILE = BASE_DIR / "afterimage_exhibitions.json"


def now():
    return datetime.now().isoformat(timespec="seconds")


def load_data(file_path):
    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 작품 관리
def get_projects():
    return load_data(PROJECTS_FILE)


def add_project(project):
    projects = get_projects()

    project["id"] = uuid.uuid4().hex
    project["created_at"] = now()
    project["updated_at"] = now()

    projects.append(project)
    save_data(PROJECTS_FILE, projects)

    return project


def update_project(project_id, updated_data):
    projects = get_projects()

    for project in projects:
        if project.get("id") == project_id:
            project.update(updated_data)
            project["updated_at"] = now()
            save_data(PROJECTS_FILE, projects)
            return True

    return False


def delete_project(project_id):
    projects = get_projects()
    filtered = [
        p for p in projects
        if p.get("id") != project_id
    ]

    save_data(PROJECTS_FILE, filtered)
    return len(filtered) != len(projects)


# 전시 관리
def get_exhibitions():
    return load_data(EXHIBITIONS_FILE)


def add_exhibition(exhibition):
    exhibitions = get_exhibitions()

    exhibition["id"] = uuid.uuid4().hex
    exhibition["created_at"] = now()
    exhibition["updated_at"] = now()

    exhibitions.append(exhibition)
    save_data(EXHIBITIONS_FILE, exhibitions)

    return exhibition


def update_exhibition(exhibition_id, updated_data):
    exhibitions = get_exhibitions()

    for exhibition in exhibitions:
        if exhibition.get("id") == exhibition_id:
            exhibition.update(updated_data)
            exhibition["updated_at"] = now()
            save_data(EXHIBITIONS_FILE, exhibitions)
            return True

    return False


def delete_exhibition(exhibition_id):
    exhibitions = get_exhibitions()
    filtered = [
        e for e in exhibitions
        if e.get("id") != exhibition_id
    ]

    save_data(EXHIBITIONS_FILE, filtered)
    return len(filtered) != len(exhibitions)
