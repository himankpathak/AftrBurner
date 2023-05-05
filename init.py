import subprocess


def RunConan(build_type):
    subprocess.run(
        (
            "conan",
            "create",
            ".",
            "--build=*",
            f"--settings=build_type={build_type}",
            "-tf=",  # Skip tests for now
        )
    )


if __name__ == "__main__":
    RunConan("MinSizeRel")
    RunConan("Debug")
