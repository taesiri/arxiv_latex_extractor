import os
import shutil
import subprocess
import tarfile
import tempfile
import time

import requests


def download_arxiv_source(arxiv_id, download_folder):
    url = f"https://arxiv.org/e-print/{arxiv_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"Failed to download the source for arXiv ID {arxiv_id}: {e}"
        )

    tar_path = os.path.join(download_folder, f"{arxiv_id}.tar.gz")
    with open(tar_path, "wb") as file:
        file.write(response.content)
    return tar_path


def extract_tar_file(tar_path, extract_folder):
    if not tarfile.is_tarfile(tar_path):
        raise RuntimeError(
            f"The downloaded file {tar_path} is not a valid tar archive."
        )
    try:
        with tarfile.open(tar_path) as file:
            file.extractall(path=extract_folder)
    except Exception as e:
        raise RuntimeError(f"Failed to extract tar file {tar_path}: {e}")


def find_and_flatten_main_tex_file(extract_folder):
    tex_files = []
    flattened_files = {}
    temp_folder = os.path.join(extract_folder, "..", "temp_flattened")
    os.makedirs(temp_folder, exist_ok=True)

    for root, _, files in os.walk(extract_folder):
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))

    for file_path in tex_files:
        try:
            temp_output_filename = os.path.basename(file_path) + "_flattened.tex"
            temp_output_path = os.path.join(temp_folder, temp_output_filename)
            file_dir = os.path.dirname(file_path)

            subprocess.run(
                ["latexpand", os.path.basename(file_path), "-o", temp_output_filename],
                cwd=file_dir,
                check=True,
                capture_output=True,
                text=True,
            )

            shutil.move(os.path.join(file_dir, temp_output_filename), temp_output_path)
            flattened_files[file_path] = temp_output_path

        except subprocess.CalledProcessError as e:
            print(f"Error processing {file_path}: {e}")

    main_file = max(
        flattened_files,
        key=lambda fp: os.path.getsize(flattened_files[fp]),
        default=None,
    )

    if main_file:
        with open(flattened_files[main_file], "r") as f:
            return f.read()

    raise RuntimeError(
        f"Main .tex file not found or could not be processed in {extract_folder}."
    )


def get_paper_content(arxiv_id: str) -> str:
    with tempfile.TemporaryDirectory() as download_folder:
        extract_folder = os.path.join(download_folder, arxiv_id)
        try:
            tar_path = download_arxiv_source(arxiv_id, download_folder)
            extract_tar_file(tar_path, extract_folder)

            content = find_and_flatten_main_tex_file(extract_folder)
            return content

        except Exception as e:
            raise e

        finally:
            pass
