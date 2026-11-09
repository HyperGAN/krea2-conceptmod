"""Lightweight installed-provider metadata; model code is loaded on creation."""
from conceptmod.contracts import BackendCapabilities
from conceptmod.providers import BackendProvider

PROVIDER = BackendProvider(
    name="krea",
    factory="krea2_conceptmod.backend:KreaBackend",
    distribution="krea2-conceptmod",
    capabilities=BackendCapabilities(),
)
