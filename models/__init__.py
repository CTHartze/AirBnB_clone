#!/usr/bin/python3
"""Manages file storage and reloading"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
