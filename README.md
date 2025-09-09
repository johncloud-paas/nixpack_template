# 🐍 Python Nixpack Template

A minimal and flexible **template repository** for packaging and deploying Python applications using [Nixpacks](https://nixpacks.com/).
This project provides a clean starting point with best practices for reproducibility, portability, and developer experience.

---

## ✨ Features

- ⚡ **Zero-config builds** with Nixpacks
- 📦 Ready-to-use `nixpacks.toml` template
- 🐍 Python 3.x runtime by default
- 🔧 Extendable with extra system dependencies
- ✅ Example project structure with `src/`, `tests/`, and `pyproject.toml`

---

## 🚀 Getting Started

Clone this template:

    git clone https://github.com/johncloud-paas/stacks/nixpack_template
    cd nixpack_template
    nixpacks build . -t my-app
    sudo docker run -p 3000:3000 my-app
