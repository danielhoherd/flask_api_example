.DEFAULT_GOAL := help

.PHONY: help
help: ## Print Makefile help
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' ${MAKEFILE_LIST} | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Clean build artifacts and delete virtualenv
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	pipenv --rm || true

.PHONY: test
test: ## Run tests
	tox
