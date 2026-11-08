from pathlib import Path
import uuid

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploaded_projects"


def save_image(uploaded_file):
    if uploaded_file is None:
        return None

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    extension = Path(uploaded_file.name).suffix.lower()
    filename = f"{uuid.uuid4().hex}{extension}"

    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return str(file_path.relative_to(BASE_DIR))


def get_image_path(image_path):
    if not image_path:
        return None

    path = BASE_DIR / image_path

    if path.exists() and path.is_file():
        return str(path)

    return None


def delete_image(image_path):
    path = get_image_path(image_path)

    if path:
        Path(path).unlink(missing_ok=True)
        return True

    return False
