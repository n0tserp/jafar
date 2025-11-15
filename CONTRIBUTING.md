# Contributing to Jafar

Thanks for your interest in Jafar! All contributions are welcome — code, docs, ideas, or bug reports.

---

## How to Contribute

### 1. Fork & Clone

git clone https://github.com/n0tserp/jafar.git

### 2. Set Up
./scripts/setup.sh
docker-compose up --build

### 3. Make Changes

- Follow PEP 8
- Add tests in tests/
- Update README.md if needed

### 4. Test
pytest tests/

### 5. Commit
git commit -m "feat: add X integration"

### 6. Open Pull Request

- Title: feat: ..., fix: ..., docs: ...
- Link to issue if exists

### Project Structure

```bash
jafar/
├── jafar/          # Core Python package
├── scripts/        # setup.sh, run_demo.sh
├── tests/          # pytest suite
├── docker-compose.yml
└── requirements.txt
```

### Good First Issues

- Add Yahoo Finance price data
- Support Canadian equities
- Add Slack alerts
- Improve Streamlit UI

## Code of Conduct
Be kind. No harassment. Respect everyone.