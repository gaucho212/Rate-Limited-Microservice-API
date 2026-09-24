# ==========================================
# Etap 1: Builder (Kompilacja i zależności)
# ==========================================
FROM python:3.12-slim AS builder

WORKDIR /app

# Instalacja zależności systemowych wymaganych do kompilacji
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Tworzenie odizolowanego wirtualnego środowiska
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==========================================
# Etap 2: Runner (Czysty, bezpieczny runtime)
# ==========================================
FROM python:3.12-slim AS runner

WORKDIR /app

# Dobra praktyka: instalacja wyłącznie bibliotek uruchomieniowych (bez kompilatorów)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Bezpieczeństwo: Utworzenie dedykowanego użytkownika bez uprawnień roota (UID 1001)
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/bash -m appuser

# Skopiowanie wyłącznie zainstalowanych bibliotek z etapu builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Optymalizacja Pythona pod kontenery: brak buforowania stdout/stderr i plików .pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Kopiowanie kodu aplikacji z przypisaniem uprawnień do appuser
COPY --chown=appuser:appgroup . .

# Przełączenie kontekstu na użytkownika nieuprzywilejowanego
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]