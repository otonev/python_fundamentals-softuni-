#!/usr/bin/env python
if __name__ == "__main__":
    version = input().split(".")
    version_number = int("".join(version))
    version_number += 1
    version = str(version_number)
    version_final = ".".join(version)
    print(version_final)
